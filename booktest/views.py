from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={}
    return render(request,'booktest/index.html', context)
    # return HttpResponse(request)

def detail(request, r1):
    return  HttpResponse(r1)

def show(request, p1, p2, p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))
# zhanshilianjie
def getTest1(request):
    return render(request, 'booktest/getTest1.html')
# 接收一键一值
def getTest2(request):
    a=request.GET['a']
    b=request.GET['b']
    context={'a':a,'b':b}
    return render(request, 'booktest/getTest2.html', context)
# 接收一键多值
def getTest3(request):
    a = request.GET['a']
    b = request.GET['b']
    return render(request, 'booktest/getTest3.html')