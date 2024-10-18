# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Task

# View to handle login and user creation
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user, created = User.objects.get_or_create(username=username)
        return redirect('task_list', user_id=user.id)
    return render(request, 'login.html')

# View to display user's tasks and handle task addition
def task_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = Task.objects.filter(user=user)
    date=Task.date
    time=Task.time

    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        if task_title:
            Task.objects.create(user=user, title=task_title)
        return redirect('task_list', user_id=user.id)

    return render(request, 'task_list.html', {'user': user, 'tasks': tasks ,})

# View to handle task deletion
def delete_task(request, task_id, user_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list', user_id=user_id)


