from django.urls import path

from contract import views

urlpatterns = [
    path("", views.index, name="index"),
]
