from django.urls import path

from . import views

app_name = "themain"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "keratin_procedure/", views.keratin_procedure, name="keratin_procedure"
    ),
    path("botox_procedure/", views.botox_procedure, name="botox_procedure"),
    path(
        "nano_plastic_procedure/",
        views.nano_plastic_procedure,
        name="nano_plastic_procedure",
    ),
    path("care_tips/", views.care_tips, name="care_tips"),
    path("price/", views.price, name="price"),]
