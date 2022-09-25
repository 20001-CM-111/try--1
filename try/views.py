from django.shortcuts import render
from .models import Try
def index(request):
    if(request.method=='POST'):
        t=Try()
        t.Name=request.POST.get('tb1')
        t.save()
    return render(request,'try/index.html')
# Create your views here.
