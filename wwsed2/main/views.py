from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import DataOfCompanies, CompanyFinancialStatements, Companies, Parametrs
from django.core.paginator import Paginator
from django.views import generic
from .forms import DataOfCompaniesForm, CompanyForm
from django.contrib.auth import authenticate, login, logout


def logout_view(request):
    logout(request)
    return redirect('/login/')

def login_view(request):
    if request.method == "POST":
        login_user = request.POST.get("login")
        password = request.POST.get("password")

        # Используем стандартный механизм аутентификации Django
        user = authenticate(request, username=login_user, password=password)

        if user is not None:
            login(request, user)
            return redirect('/main/')
        else:
            # Если учетные данные неверные, возвращаем пользователя на страницу логина с сообщение об ошибке
            return render(request, "registration/login.html", {"error": "Неверные логин или пароль"})
    else:
        return render(request, "registration/login.html", {})

class CompanyCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/createcompanies.html'
    form_class = CompanyForm

    def form_valid(self, form):
        company = form.save()
        return redirect('createdataofcompany', company_id=company.id)


class DataOfCompaniesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/createdataofcompanies.html'
    form_class = DataOfCompaniesForm

    def get_initial(self):
        company_id = self.kwargs.get('company_id')
        return {'companies': company_id}
    success_url = '/main/'


class companySearch(LoginRequiredMixin, generic.ListView):
    model = DataOfCompanies
    template_name = 'main/companysearch.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = DataOfCompanies.objects.filter(
            companies__name__icontains=query
        )
        return object_list


@login_required
def companieslist(request):
    datas = DataOfCompanies.objects.all().order_by('id')  # Упорядочивание данных

    paginator = Paginator(datas, 50)  # 50 компаний на странице
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'main/companieslist.html', context)

@login_required
def companyPage(request, companies_id):
    companyStatements2023 = CompanyFinancialStatements.objects.filter(companies=companies_id, year=2023)

    if companyStatements2023.exists():
        parametrs_set = list(Parametrs.objects.values_list("name", flat=True).order_by("id"))

        # Инициализация параметров
        parametr_dict = {param_id: None for param_id in range(1, 10)}

        for statement in companyStatements2023:
            parametr_dict[statement.parametr.id] = statement

        years_list = CompanyFinancialStatements.objects.filter(companies=companies_id).values_list("year", flat=True).distinct()
        years_and_statements_values = []

        # Словарь для хранения значений по каждому параметру
        parametrs_data = {param_id-1: [] for param_id in range(1, 10)}

        for year in years_list:
            values_for_year = CompanyFinancialStatements.objects.filter(companies=companies_id, year=year).order_by("parametr_id").values_list("value", flat=True)
            years_and_statements_values.append((year, values_for_year))

            # Заполнение данных по каждому параметру
            for param_id in parametrs_data:
                statement = CompanyFinancialStatements.objects.filter(companies=companies_id, year=year, parametr__id=param_id+1).first()
                if statement:
                    parametrs_data[param_id].append((year, statement.value))

        # Подготовка данных для использования в шаблоне
        parametrs_json_data = {
            param_id: {
                'years': [year for year, _ in data],
                'values': [value for _, value in data]
            }
            for param_id, data in parametrs_data.items()
        }

        # Получение данных компании
        company_data = DataOfCompanies.objects.filter(companies_id=companies_id).first()

        context = {
            'parametrs_set': parametrs_set,
            'years_and_statements_values': years_and_statements_values,
            'parametrs_json_data': parametrs_json_data,
            'company_data': company_data,
            **parametr_dict
        }
        return render(request, 'main/companypage.html', context)

    else:
        company = get_object_or_404(Companies, id=companies_id)
        return render(request, 'main/emptycompanypage.html', {'company': company})