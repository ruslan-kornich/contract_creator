from django.http import FileResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from contract.services.agreement_date import get_agreement_date
from contract.services.bank_detail import get_bank_name, get_mfo_code
from contract.services.get_company_details import get_company_info
from contract.services.get_fop_details import get_fop_info
from .forms import ContractForm
from .services.create_contract import contract_create


def index(request):
    user = request.user
    if request.method == "POST":
        form = ContractForm(request.POST, user=user)
        if form.is_valid():
            return HttpResponseRedirect("/create/")
    else:
        form = ContractForm(user=user)
    return render(request, "contract/index.html", {"form": form})


def create(request):
    if request.method == "POST":
        code = request.POST["code_company"]
        bank_account = request.POST["bank_account"]
        template = request.POST["template_choices"]
        data = get_fop_info(code) if len(code) == 10 else get_company_info(code)
        mfo = get_mfo_code(bank_account)
        bank_name = get_bank_name(mfo)
        if data:
            bank_data = {
                "bank_account": bank_account,
                "bank_name": bank_name,
                "mfo": mfo,
                "date_generate": get_agreement_date(),
            }
            data.update(bank_data)
            template_path = "media/" + template
            response = FileResponse(open(contract_create(data, template_path), "rb"))

            return response

        else:
            return HttpResponseRedirect("/no-data/")


def no_data(request):
    return render(request, "contract/no_data.html", {})
