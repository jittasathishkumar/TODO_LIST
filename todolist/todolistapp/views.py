from django.shortcuts import render,redirect
from datetime import datetime   
from .models import todoclass

# Create your views here.
def Index(request):
    if request.method=='GET':
        row=todoclass.objects.all()
        return render(request,'Index.html',{'rows':row})
    else:
        todoclass(
        title=request.POST.get('title'),
        Details=request.POST.get('Details'),
        date=datetime.now()
        ).save()
        row=todoclass.objects.all()
        return render(request,'Index.html',{'rows':row})
      



def update(request,id):
    row=todoclass.objects.get(id=id)
    return render(request,'upd.html',{'row':row})

def updated(request,id):
    row=todoclass.objects.get(id=id)
    row.title = request.POST.get('title')
    row.Details = request.POST.get('Details')
    row.save()
    return redirect(Index)

def clear(request,id):
    data=todoclass.objects.get(id=id)
    data.delete()
    return redirect(Index)