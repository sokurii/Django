from django.urls import path
from . import views

# 중복을 막기 위해 app name 설정
app_name = 'pages'
urlpatterns = [
    # path의 세 번째 인자에 이름 적어주기 
    # name을 사용해서 url 접근하기 
    path('qwer/',views.qwer,name='qwer'),
    path('asdf/',views.asdf,name='asdf'),
]