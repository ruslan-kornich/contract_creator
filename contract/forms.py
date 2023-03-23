from django import forms


class ContractForm(forms.Form):
    code_company = forms.CharField(label="Code your company", max_length=10)
    bank_account = forms.CharField(label="Bank account", max_length=30)
