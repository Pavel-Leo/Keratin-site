from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path("group/<slug:slug>/", views.posts, name="post"),
]