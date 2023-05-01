from django.shortcuts import render
from.models import Registration 


# Create your views here.
def home(req):
    return render(req,'index.html')
def insert(req):
    ob=Registration()
    ob.name=req.GET.get('name')
    ob.email=req.GET.get('email')
    ob.contact=req.GET.get('number')
    ob.age=req.GET.get('age')
    ob.village=req.GET.get('village')
    ob.save()
    return render(req,'index.html')


    
