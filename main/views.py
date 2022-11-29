
from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def showData(request):
    data = Covid19.objects.all()
    return(render(request, "show_data.html", {"data" : data}))

def addData(request):
    form = CovidDataForm(request.POST)
    if(form.is_valid()):
        form.save()
        return(redirect("/"))
    return(render(request, "add_data.html" , {"form" : form}))