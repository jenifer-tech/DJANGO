from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(30)
def home(request):
    return render(request,'app/course.html')
@cache_page(30)
def contact(request):
    return render(request,'app/contact.html')    

