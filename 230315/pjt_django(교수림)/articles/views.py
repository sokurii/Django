from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

# def index(request):
#     return HttpResponse("<h1>hello, world</h><br><h1>Hello, I'm Jinhee :D</h>")

# def index(request):
#     return HttpResponse("""
#     <h1>안녕하세요<h1>
#     <h2>저는 박진희입니다<h2>
#     """)
    