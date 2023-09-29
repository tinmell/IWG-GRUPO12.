from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def hello(request):
    title= 'Bienvenido'
    return render(request, 'hello.html')
#HttpResponse("<h2>Hola mundo</h2>")
def about(request):
    return HttpResponse('About')