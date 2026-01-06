from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 5
    y = 10
    return x
# Create your views here.
def say_hello(request):
    x = calculate()
    return render(request, 'playground.html', {'name': 'Maxtar Ov'})