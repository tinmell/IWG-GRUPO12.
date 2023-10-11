from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Task
from .forms import introform
# Create your views here.
def hello(request):
    title= 'Bienvenido'
    return render(request, 'hello.html')
#HttpResponse("<h2>Hola mundo</h2>")


def about(request):
    return HttpResponse('About')

