# Create your views here.

from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Task

def index(request):
    tasks = Task.objects.all().order_by('priority')  # Ordenar por prioridad
    data = serialize("python", tasks)
    return JsonResponse(data, safe=False)
