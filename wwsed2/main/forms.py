from django import forms
from django.forms import ModelForm
from .models import DataOfCompanies, Companies, Parametrs


class CompanyForm(ModelForm):
    class Meta:
        model = Companies
        fields = ('name', )

class DataOfCompaniesForm(ModelForm):
    class Meta:
        model = DataOfCompanies
        fields = ('companies', 'type', 'inn', 'ogrn')




