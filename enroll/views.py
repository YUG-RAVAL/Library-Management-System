from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import BookRegistraion
from .models import lib
# Create your views here.
#This function will add items and show
def add(request):
    if request.method == 'POST':
        fm = BookRegistraion(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ds = fm.cleaned_data['description']
            reg = lib(name=nm, description=ds)
            reg.save()
            fm = BookRegistraion()
        
    else:
       fm = BookRegistraion() 
    book = lib.objects.all()
    return render(request,'enroll/add.html',{'form':fm,'buk':book})


#This Function will update records
def update(request, id):
    if request.method=="POST":
        pi = lib.objects.get(pk=id)
        fm = BookRegistraion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = lib.objects.get(pk=id)
        fm = BookRegistraion(instance=pi)
        
    return render(request,'enroll/update.html',{'form':fm})



#This function will delete
def delete(request, id):
    if request.method=='POST':
        pi = lib.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')