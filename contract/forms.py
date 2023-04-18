from django import forms


class ContractForm(forms.Form):
    code_company = forms.CharField(label="Code your company", max_length=10)
    bank_account = forms.CharField(label="Bank account", max_length=30)
    template_choices = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["template_choices"].choices = [
            (template.file, template.name) for template in user.templates.all()
        ]
