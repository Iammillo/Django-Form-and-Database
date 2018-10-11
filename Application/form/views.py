from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .forms import NameForm
import json
# Create your views here.

def index(request):
    return render(request, "index.html")

def submit(request):
    if request.method=='POST':
        form1 = NameForm(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data;
            obj=models.MyDB.objects.all().filter(Roll=data["Roll"])
            if obj.exists():
                obj.update(Name=data["Name"],Address=data["Address"], Roll=data["Roll"].upper(), Contact=data["mobile"], Available=data["Available"])
            else:
                models.MyDB(Name=data["Name"],Address=data["Address"], Roll=data["Roll"].upper(), Contact=data["mobile"], Available=data["Available"]).save()

            x={"message":"Your Form is Submitted.", "color":"text-success"}
            return render(request,'index.html',x)
        else:
            x={"message":"You Submitted Invalid Form.","color":"text-danger"}
            return render(request,'index.html',x)
    else:
        return render(request, "index.html")




def search(request):
    if request.method=='POST':
        data = request.POST.get("str","")
        obj = models.MyDB.objects.all().filter(Roll=data.upper())
        if obj.exists():
            reply={"Name":obj[0].Name,"Address":obj[0].Address, "Roll":obj[0].Roll, "Contact":obj[0].Contact, "Available":obj[0].Available}
            reply=json.dumps(reply,sort_keys=True)
            return HttpResponse(reply)
        else:
            return HttpResponse("Not Found")
