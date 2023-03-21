from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):   
    articles = Article.objects.all()    # DB에서 모!든! Article 가져오기(articles)
    context = {'articles' : articles}   # context로 articles 넘겨주기 
    return render(request,'articles/index.html', context) # 두번째 파라미터에 템플릿 경로 넘겨주기(템플릿 만들어야 함)

def detail(request,pk):
    article = Article.objects.get(id=pk) # 한 개의 Article 조회(article)
    context = {'article':article}        # 한 개의 조회한 article context에 받아서 보내주기
    return render(request, 'articles/detail.html',context)

def new(request):               # 비어있는 form 화면 보여주면 됨
    return render(request,'articles/new.html')      

def create(request):   
    # [1] 사용자가 전송한 데이터(request) 가져온다        
    title = request.POST.get('title')     
    content = request.POST.get('content')  
    print(title,content)

    # [2] DB에 새로운 Article 저장한다
    # Article.objects.create(
    #     title=title,
    #     content=content
    # )

    # 데이터 저장 전 유효성 검사 위해 
    article = Article(title=title, content=content)
    article.save()


    # [3] 저장한 걸 index 페이지로 보낸다
    return redirect('articles:index') 


def delete(request,pk):
    article = Article.objects.get(pk=pk)    # 한 개의 Article 조회(article)
    article.delete()                        # 해당 article 삭제
    return redirect('articles:index')       # 그 결과값 반영한 index 페이지 찾아감 

def edit(request,pk):
    article = Article.objects.get(pk=pk)    # 한 개의 Article 조회(article)
    context = {'article':article}           # 조회한 article context에 받아서 보내주기
    return render(request, 'articles/edit.html', context)   # 템플릿 경로 넘겨주기

def update(request,pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', pk= article.pk)
