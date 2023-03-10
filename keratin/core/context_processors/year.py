from django.utils import timezone as tz


def year(request):
    """Добавляет переменную с текущим годом."""
    request = tz.now().year
    return {"year": request}
