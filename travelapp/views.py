from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def home(request):
    obj = place.objects.all()
    obj1= team.objects.all()
    return render(request, "index.html",{'result':obj,'team':obj1})

# def result(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request, "result.html",{'add':add,'sub':sub,'mul':mul,'div':div})
