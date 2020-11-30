from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def index_add_task(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        due_date = request.POST.get("due_date", "")
        task = Task(name=name, due_date=due_date)
        task.save()
        return redirect('/')
    else:
        tasks = Task.objects.all()
        return render(request, 'todo_app/index.html', {'tasks': tasks})



def complete_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request, 'todo_app/confirm-complete.html')
