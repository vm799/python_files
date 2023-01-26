from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def work_experience(request):
    return render(request, 'index2.html')

def projects(request):
    return render(request, 'index3.html')