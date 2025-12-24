from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    p=1
    t=2
    return render(request, 'playground.html', {'name': 'Maxtar Ov'})