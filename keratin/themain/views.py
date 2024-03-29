from django.shortcuts import render


def index(request):
    template = "themain/index.html"
    title = "Главная страница"
    context = {"title": title}
    return render(request, template, context)


def keratin_procedure(request):
    template = "themain/keratin_procedure.html"
    title = "Кератиновое выпрямление"
    context = {
        "title": title,
    }
    return render(request, template, context)


def botox_procedure(request):
    template = "themain/botox_procedure.html"
    title = "Ботоксное разглаживание"
    context = {
        "title": title,
    }
    return render(request, template, context)


def nano_plastic_procedure(request):
    template = "themain/nano_plastic_procedure.html"
    title = "Нанопластика"
    context = {
        "title": title,
    }
    return render(request, template, context)


def care_tips(request):
    template = "themain/care_tips.html"
    title = "Советы по уходу"
    context = {
        "title": title,
    }
    return render(request, template, context)


def price(request):
    template = "themain/price.html"
    title = "Прайс"
    context = {
        "title": title,
    }
    return render(request, template, context)


def about(request):
    template = "core/404.html"
    title = "О нас"
    context = {
        "title": title,
    }
    return render(request, template, context)
