from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContractForm


def index(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/create/")
    else:
        form = ContractForm()
    return render(request, "contract/index.html", {"form": form})


def create(request):
    pass