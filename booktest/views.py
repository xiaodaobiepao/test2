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

# jieshouyijianyizhi

def getTest2(request):
    a=request.GET['a']
    b=request.GET['b']
    context={'a':a,'b':b}
    return render(request, 'booktest/getTest2.html', context)
# jiehsouyijianduozho,bunegyouzhongwen

def getTest3(request):
    a = request.GET.getlist('a')
    b = request.GET['b']
    context={'a':a}
    return render(request, 'booktest/getTest3.html',context)

def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    return render(request,'booktest/postTest2.html')