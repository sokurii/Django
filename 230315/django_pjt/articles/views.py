from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'sokurii'
    return render(request,'articles/index.html',{'name':name})