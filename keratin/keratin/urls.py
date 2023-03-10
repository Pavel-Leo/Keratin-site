from django.contrib import admin
from django.urls import include, path

handler404 = "core.views.page_not_found"

urlpatterns = [
    path('', include("themain.urls", namespace="themain")),
    path('admin/', admin.site.urls),
]
