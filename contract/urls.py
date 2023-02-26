from django.urls import path

from contract import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("no-data/", views.no_data, name="no-data"),
]
