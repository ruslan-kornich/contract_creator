from django.contrib import admin

from contract.models import Company, Template, ContractFile, Contract

admin.site.register(Company)
admin.site.register(Template)
admin.site.register(ContractFile)
admin.site.register(Contract)
