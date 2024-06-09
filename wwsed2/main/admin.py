from django.contrib import admin
from .models import CompanyFinancialStatements, Companies, TypeOfActivity, Parametrs, DataOfCompanies

class CompanyFinancialStatementsAdmin(admin.ModelAdmin):
    list_display = ('companies', 'parametr', 'year', 'value', 'data_source', 'trust_level')

class DataOfCompaniesAdmin(admin.ModelAdmin):
    list_display = ('companies', 'type', 'inn', 'ogrn')

admin.site.register(CompanyFinancialStatements, CompanyFinancialStatementsAdmin)
admin.site.register(DataOfCompanies, DataOfCompaniesAdmin)
admin.site.register(Companies)
admin.site.register(TypeOfActivity)
admin.site.register(Parametrs)