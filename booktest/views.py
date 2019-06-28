from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST.get('ugender')
    uhobby=request.POST.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)

def cookieTest(request):
    response=HttpResponse()
    response.set_cookie('t1','abbc')
    return response

def redTest1(request):
    return HttpResponseRedirect('booktest/redTest2')

def redTest2(request):
    return HttpResponse('zheshizhuanxiangdeyemian')

def session(request):
    uname=request.session.get('myname')
    context={'uname':uname}
    return render(request,'booktest/session.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session_handle(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    request.session['myname']=uname
    return HttpResponseRedirect('booktest/session')