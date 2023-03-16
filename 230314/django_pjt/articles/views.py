from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('<h1>그래</h1>')

def index(request):
    return render(request, "articles/index.html")