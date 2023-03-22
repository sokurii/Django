from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):

    if request.method == "POST":
        pass
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():                         # 로그인에 성공하면
            auth_login(request, form.get_user())
            print('--<-<-<@ 로그인에..성공하셨습니다..')
            return redirect('articles:index')    # 인덱스 페이지로 ㄱㄱ(다른 앱의 뷰 함수 호출 ~! )
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)




def logout(request):
    auth_logout(request)
    print('저..갑니다..')
    return redirect('accounts:login')
