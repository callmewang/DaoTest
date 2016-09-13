from django.shortcuts import render
from django.http import HttpResponse
from  datetime import datetime



def home(request):
    print 'home----------------'
    return render(request,'template.html',{'current_time': datetime.now()})