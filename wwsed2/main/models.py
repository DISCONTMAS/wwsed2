# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Companies(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'companies'

    def __str__(self):
        return self.name


class CompanyFinancialStatements(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies = models.ForeignKey(Companies, models.DO_NOTHING)
    parametr = models.ForeignKey('Parametrs', models.DO_NOTHING)
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements'


class CompanyFinancialStatements2013(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2013'


class CompanyFinancialStatements2014(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2014'


class CompanyFinancialStatements2015(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2015'


class CompanyFinancialStatements2016(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2016'


class CompanyFinancialStatements2017(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2017'


class CompanyFinancialStatements2018(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2018'


class CompanyFinancialStatements2019(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2019'


class CompanyFinancialStatements2020(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2020'


class CompanyFinancialStatements2021(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2021'


class CompanyFinancialStatements2022(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2022'


class CompanyFinancialStatements2023(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2023'


class CompanyFinancialStatements2024(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2024'


class CompanyFinancialStatements2025(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2025'


class CompanyFinancialStatements2026(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2026'


class CompanyFinancialStatements2027(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2027'


class CompanyFinancialStatements2028(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2028'


class CompanyFinancialStatements2029(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2029'


class CompanyFinancialStatements2030(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companies_id = models.IntegerField()
    parametr_id = models.IntegerField()
    year = models.IntegerField()
    value = models.CharField(max_length=300)
    data_source = models.IntegerField()
    trust_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_financial_statements2030'


class DataOfCompanies(models.Model):
    companies = models.ForeignKey('Companies', models.DO_NOTHING)
    type = models.ForeignKey('TypeOfActivity', models.DO_NOTHING)
    inn = models.CharField(db_column='INN', max_length=64)  # Field name made lowercase.
    ogrn = models.CharField(db_column='OGRN', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_of_companies'


class Parametrs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'parametrs'

    def __str__(self):
        return self.name


class TypeOfActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'type_of_activity'

    def __str__(self):
        return self.name
