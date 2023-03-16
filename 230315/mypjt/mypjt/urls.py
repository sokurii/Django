"""mypjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from articles import views

urlpatterns = [
    # 입력받을 경로 설정 
    # app 많아지면 url도 늘어남 
    
    path('admin/', admin.site.urls),
    # 각 app의 urls로 연결 
    path('articles/', include('articles.urls')),
    path('pages/',include('pages.urls')),
]
