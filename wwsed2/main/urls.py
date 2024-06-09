from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (companieslist, companyPage, companySearch,
                    CompanyCreateView, DataOfCompaniesCreateView, login_view, logout_view,
                    )

urlpatterns = [
    path('', companieslist, name='companieslist'),
    path('add/<int:company_id>', DataOfCompaniesCreateView.as_view(), name='createdataofcompany'),
    path('add/', CompanyCreateView.as_view(), name='add_company'),
    path('<int:companies_id>/', companyPage, name='company_page'),
    path('search/', companySearch.as_view(), name='search_company'),
    path('login/', login_view, name='login'),  # Добавляем путь для логина
    path('logout/', logout_view, name='logout'),  # Добавляем путь для выхода

]