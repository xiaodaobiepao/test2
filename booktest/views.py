from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={}
    return render(request,'booktest/index.html', context)

def detail(request, r1):
    return  HttpResponse(r1)

def show(request, p1, p2, p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))