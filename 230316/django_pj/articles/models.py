from django.db import models

# Create your models here.

# 데이터베이스를 어떻게 저장할 지 
class Article(models.Model):
    title = models.CharField(max_length=10) # 글자(char)로 제목저장, 최대 저장 글자 수  
    content = models.TextField()
