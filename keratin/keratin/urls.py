from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("themain.urls", namespace="themain")),
    path('admin/', admin.site.urls),
]
