from django.http import JsonResponse


def index(request):
    return JsonResponse({"message": "Django lab (dependances anciennes)", "status": "ok"})
