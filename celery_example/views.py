from django.shortcuts import render

# Create your views here.
#celery_example/views.py
from django.shortcuts import render, HttpResponse
from .tasks import prueba_suma, enviar_mail
# Create your views here.

def index(request):

    #enviar_mail.delay("Celery", "Esto es una prueba de Celery", "lean_vega1@hotmail.com")
    prueba_suma.delay(5,6)

    return HttpResponse("Hola")