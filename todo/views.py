from django.shortcuts import redirect, get_object_or_404, render
from .models import Task

# Create your views here.

def addTask(Request):
    task= Request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(Request, pk):
    task= get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def markAsUndone(Request, pk):
    task= get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def editTask(Request, pk):
    getTask= get_object_or_404(Task,pk=pk)
    if Request.method=="POST":
        newTask= Request.POST['task']
        getTask.task= newTask
        getTask.save()
        return redirect('home')
    else:
        context = {
            "getTask":getTask,
        }
        return render(Request, 'editTask.html', context)

def deleteTask(Request, pk):
    getTask= get_object_or_404(Task,pk=pk)
    getTask.delete()
    return redirect('home')