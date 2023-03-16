from django.shortcuts import render

# Create your views here.
# qwer로 요청이 들어오면 화면에 '하하하' 뿌려보센.. 
def qwer(request):
    msg = '하하하'
    return render(request, 'pages/qwer.html',{'data':msg})


def asdf(request):
    msg = '호호호'
    return render(request,'pages/asdf.html',{'data':msg} )