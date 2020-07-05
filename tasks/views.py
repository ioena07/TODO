from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


def index(request):
    tasks = Tasks.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"tasks": tasks, "form": form}
    return render(request, "tasks/list.html", context)


def updateTask(request, pk):  # pk = primary key, poate fi orice nume
    task = Tasks.objects.get(id = pk)
    form = UpdateForm(instance = task)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "tasks/update_tasks.html", context)


def deleteTask(request, pk):
    item = Tasks.objects.get(id = pk)
    
    if request.method == "POST":
        item.delete()
        return redirect("/")
    context = {"item": item}
    return render(request, "tasks/delete.html", context)
