from django.shortcuts import render
import datetime
# Create your views here.
def info_view(request):
    date=datetime.datetime.now()
    name="Django"
    prerequirments="Python"
    return render(request,'testapp/result.html',{'msg':date,'name':name,'pre':prerequirments})