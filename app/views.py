from django.shortcuts import render
from.models import Resum
from.forms import ResumForm
from django.views import View

# Create your views here.
class HomePage(View):
    def get(self,request):
        fm=ResumForm()
        return render(request,'home.html',{'form':fm})
    
    def post(self,request):
        fm=ResumForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            
        return render(request,'home.html',{'form':fm})
    

