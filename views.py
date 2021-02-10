from django.shortcuts import render
from django.http import HttpResponse
from company.models import Student

# Create your views here.
def home_view(request):
    key=Student.objects.all()
    return render(request,"indexx.html",{'data':key})
