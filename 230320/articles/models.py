from django.db import models

# Create your models here.

# 타이틀, 내용 필요
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # =>모델에 대한 변경사항 생겼으므로, makemigraitons & migrate 해주기  

    # 매직메서드 오버라이딩
    # 상위클래스 정의된 메서드와 동작을 달리 해주고 싶을 때 
    def __str__(self):
        return f'{self.id}번째 글 - {self.title}'