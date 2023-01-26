from django.shortcuts import render


def index(request):
    template = 'themain/index.html'
    title = "Последние обновления на сайте"
    caption = "Последние обновления на сайте"
    context = {
        "title": title,
        "caption": caption,
    }
    return render(request, template, context)


def posts(request, slug):
    pass