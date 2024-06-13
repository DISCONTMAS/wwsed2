from django import forms
from django.forms import ModelForm
from .models import DataOfCompanies, Companies, Parametrs, TypeOfActivity


class CompanyForm(ModelForm):
    class Meta:
        model = Companies
        fields = ('name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем класс 'form-control' ко всем полям
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class DataOfCompaniesForm(ModelForm):
    class Meta:
        model = DataOfCompanies
        fields = ('companies', 'type', 'inn', 'ogrn')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем класс 'form-control' ко всем полям
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class CompanySearchForm(forms.Form):
    type = forms.ModelChoiceField(
        queryset=TypeOfActivity.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Вид деятельности'
    )
    inn = forms.CharField(
        max_length=64,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='ИНН'
    )
    ogrn = forms.CharField(
        max_length=64,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='ОГРН'
    )