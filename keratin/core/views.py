from django.http import HttpResponse
from django.shortcuts import render


def page_not_found(request, exception) -> HttpResponse:
    return render(request, "core/404.html", {"path": request.path}, status=404)
