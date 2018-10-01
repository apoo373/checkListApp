# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import ItemForm

def Login(request):
    return HttpResponseRedirect('/admin/login')

def Logout(request):
    return HttpResponseRedirect('/admin/logout')

# All items
@login_required
def myChecklist(request):
    list = CheckList.objects.filter(userId=request.user.id).order_by('-priority')
    context = {
        'checklist': list,
    }
    return render(request, 'checklist/index.html', context)

# Category Items
@login_required
def itemsByCategory(request, category_name):
    print category_name
    list = CheckList.objects.filter(userId=request.user.id, category=category_name.upper()).order_by('-priority')
    context = {
        'checklist': list,
    }
    return render(request, 'checklist/index.html', context)

# Single Items
@login_required
def getitem_byId(request, item_id):
    try:
        requested_item = CheckList.objects.get(pk=item_id, userId=request.user.id)
    except CheckList.DoesNotExist:
        raise Http404("Either Item Does Not Exist. Or You Don't have Permission to view it")
    return render(request, 'checklist/singleItem.html', {'requested_item': requested_item})

# Delete and Reactivate Item
@login_required
def deleteItem(request, item_id):
    try:
        itemToBeDeleted = CheckList.objects.get(pk=item_id, userId=request.user.id)
    except Question.DoesNotExist:
        raise Http404("Either Item Does Not Exist. Or You Don't have Permission to Delete it")
    itemToBeDeleted.delete()
    return redirect('myChecklist')

# Completed and Non-Completed Items
@login_required
def completeItem(request, item_id):
    try:
        itemToBeCompleted = CheckList.objects.get(pk=item_id, userId=request.user.id)
    except Question.DoesNotExist:
        raise Http404("Either Item Does Not Exist. Or You Don't have Permission to Delete it")
    itemToBeCompleted.isCompleted = True
    itemToBeCompleted.save()
    return render(request, 'checklist/singleItem.html', {'requested_item': itemToBeCompleted})

def reopenItem(request, item_id):
    try:
        reopenItem = CheckList.objects.get(pk=item_id, userId=request.user.id)
    except Question.DoesNotExist:
        raise Http404("Either Item Does Not Exist. Or You Don't have Permission to Reactivate it")
    reopenItem.isCompleted = False
    reopenItem.save()
    return render(request, 'checklist/singleItem.html', {'requested_item': reopenItem})

# Edit Existing Items
@login_required
def editItmes(request, item_id):
    try:
        requestedItem = CheckList.objects.get(pk=item_id, userId=request.user.id)
    except CheckList.DoesNotExist:
        raise Http404("Either Item Does Not Exist. Or You Don't have Permission to Edit it")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST, instance=requestedItem)
        # check whether it's valid:
        if form.is_valid():
            editItem = form.save(commit=False)
            editItem.category = editItem.category.upper()
            editItem.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/checklist/' + item_id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm(instance=requestedItem)
    return render(request, 'checklist/edititems.html', {'form': form, 'item': item_id})


# Create Item
@login_required
def createItem(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newItem = form.save(commit=False)
            newItem.userId = request.user
            newItem.category = newItem.category.upper()
            newItem.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/checklist/' + str(newItem.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemForm()
    return render(request, 'checklist/createItem.html', {'form': form})
