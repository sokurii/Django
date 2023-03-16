# render를 사용해서 html 문서에서 통으로 끌고 와서 화면에 뿌리겠다 
from django.shortcuts import render
import random

# Create your views here.
# 클라이언트로부터 서버가 request를 받음 

def index(request):

    # 서버가 화면에 뿌릴 때(?) -- index.html에도 넣어주기 
    name = 'park'
    # render의 세 번째 매개변수에 객체형태로(딕셔너리) 올려준 뒤 뿌리기(?렌더링?)
    return render(request, 'articles/index.html',{'name':name}) # templates에 있는 articles파일 




def greeting(request):

    name = ['heo','park','kim']
    foods = ['스테이크','샤브샤브','마라탕']

    # 조건에 따라(요청에 따라) 랜덤으로 출력하기 
    pick = random.choice(foods)
    context = {
        'names':name,
        'foods':foods,
        'pick':pick,
    } 
    # 세 번째 매개변수에..
    return render(request, 'articles/greeting.html',context) # templates에 있는 articles파일 


# hi = '안녕하세요'

# # qwer로 요청이 들어오면 화면에 '하하하' 뿌려보센.. 
# def qwer(request):
#     msg = '하하하'
#     return render(request, 'articles/qwer.html',{'data':msg})


# def asdf(request):
#     msg = '호호호'
#     return render(request,'articles/asdf.html',{'data':msg} )