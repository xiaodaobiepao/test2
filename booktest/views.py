from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'booktest/index.html', context)

def detail(request, r1):
    return  HttpResponse(r1)