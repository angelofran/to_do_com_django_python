from django.shortcuts import render, get_object_or_404, redirect
from .forms import dist1_form
from .models import dist1
from django.contrib import  messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

@login_required
def home(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter') 
    task_done_rencently = dist1.objects.filter(done='done', update_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    task_done = dist1.objects.filter(done='done', user=request.user).count()
    task_doing = dist1.objects.filter(done='doing', user=request.user).count()
    if search:
        tasks = dist1.objects.filter(title__icontains=search, user=request.user)
    elif filter:
        tasks = dist1.objects.filter(done=filter, user=request.user)
    else:
        tasks_list = dist1.objects.all().order_by('-creat_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'home.html', {'tasks': tasks, 'taskdonerencent':task_done_rencently, 'taskdone':task_done, 'taskdoing':task_doing})

@login_required
def taskView(request, id):
    task = get_object_or_404(dist1, pk=id)
    return render(request, 'task.html', {'task': task})

@login_required
def NewTask(request):
    if request.method == 'POST':
        form = dist1_form(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/home/')
    else:
        form = dist1_form()
        return render(request, 'addtask.html', {'form': form})

@login_required
def EditTask(request, id):
    task = get_object_or_404(dist1, pk=id)
    form = dist1_form(instance=task)

    if request.method == 'POST':
        form = dist1_form(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/home/')
        else:
            return render(request, 'edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'edittask.html', {'form': form, 'task': task})

@login_required
def DelTask(request, id):
    task = get_object_or_404(dist1, pk=id)
    task.delete()
    messages.info(request, 'Tarefa foi deletada.')
    return redirect('/home/')

@login_required
def checktask(request, id):
    task = get_object_or_404(dist1, pk=id)
    if task.done == 'doing':
        task.done = 'done'
    else:
        task.done = 'doing'

    task.save()
    return redirect('/home')
