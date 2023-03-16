from django.urls import path
from . import views

# 중복을 막기 위해 app name 설정
app_name = 'articles'
urlpatterns = [
    # path의 세 번째 인자에 이름 적어주기 
    # name을 사용해서 url 접근하기 
    path('index/',views.index, name='index'),
    path('greeting/',views.greeting, name='greeting'),
]