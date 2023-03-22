from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # ''에 매칭되면(articles/에 들어오면) views.index에서 처리해줘
    path('',views.index, name='index'),
    # 숫자가 들어오면 id로 받아서 views.detail에서 처리해줘 
    path('<int:pk>/',views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    
]
