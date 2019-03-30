from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

#Import the class List from models to usage in views
#We use "dot" to denote that List should be important from models in parent class before trying in any place else


def home(request):
    if request.method=='POST':
        form=ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items=List.objects.all #Get all the objects from the List
            messages.success(request, ("Item has been added to the List!"))
            return render(request, 'home.html', {'all_items': all_items })
    else:
        all_items=List.objects.all #Get all the objects from the List
        return render(request, 'home.html', {'all_items': all_items })

def about(request):
    context={"first_name":"Ajitesh", "last_name": "Abhishek"}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item has been deleted!"))
    return redirect('home')

def cross_off(request, list_id):
    item=List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    messages.success(request, ("Congratulations for completing the item!"))
    return redirect('home')

def uncross_off(request, list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    messages.success(request, ("Item has been uncrossed!"))
    return redirect('home')

def edit(request, list_id):
    if request.method=='POST':
        item=List.objects.get(pk=list_id)

        form=ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ("Item has been edited"))
            return redirect('home')
    else:
        item=List.objects.get(pk=list_id) #Get all the objects from the List
        return render(request, 'edit.html', {'item': item})
