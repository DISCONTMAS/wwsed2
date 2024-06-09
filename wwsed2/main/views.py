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

        revenue = average_salary = number_of_employees = percentage_of_women = date_of_the_report = None
        participation_in_charity = debt = share = foreign_employees = None

        for statement in companyStatements2023:
            if statement.parametr.id == 1:
                revenue = statement
            elif statement.parametr.id == 2:
                average_salary = statement
            elif statement.parametr.id == 3:
                number_of_employees = statement
            elif statement.parametr.id == 4:
                percentage_of_women = statement
            elif statement.parametr.id == 5:
                date_of_the_report = statement
            elif statement.parametr.id == 6:
                participation_in_charity = statement
            elif statement.parametr.id == 7:
                debt = statement
            elif statement.parametr.id == 8:
                share = statement
            elif statement.parametr.id == 9:
                foreign_employees = statement

        years_list = CompanyFinancialStatements.objects.filter(companies=companies_id).values_list("year",
                                                                                                   flat=True).distinct()
        years_and_statements_values = []

        revenue_by_year = []

        for year in years_list:
            values_for_year = CompanyFinancialStatements.objects.filter(companies=companies_id, year=year).order_by(
                "parametr_id").values_list("value", flat=True)
            years_and_statements_values.append((year, values_for_year))

            # Get revenue for the year
            revenue_statement = CompanyFinancialStatements.objects.filter(companies=companies_id, year=year,
                                                                          parametr__id=1).first()
            if revenue_statement:
                revenue_by_year.append((year, revenue_statement.value))

        # Separate years and revenues for use in the template
        years = [year for year, _ in revenue_by_year]
        revenues = [revenue for _, revenue in revenue_by_year]

        context = {
            'revenue': revenue,
            'average_salary': average_salary,
            'number_of_employees': number_of_employees,
            'percentage_of_women': percentage_of_women,
            'date_of_the_report': date_of_the_report,
            'participation_in_charity': participation_in_charity,
            'debt': debt,
            'foreign_employees': foreign_employees,
            'share': share,
            'parametrs_set': parametrs_set,
            'years_and_statements_values': years_and_statements_values,
            'years': years,
            'revenues': revenues
        }
        return render(request, 'main/companypage.html', context)

    else:
        company = get_object_or_404(Companies, id=companies_id)
        return render(request, 'main/emptycompanypage.html', {'company': company})
