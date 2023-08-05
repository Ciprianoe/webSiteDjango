from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project,Task
from .forms import CreateNewTask,CreateNewProject

""" para devolver error en django """
from django.shortcuts import get_object_or_404 

# Create your views here.
def home(request):
    title = "Django App!!!!"
    active = 'home'
    return render(request,'index.html', {
        "active":active,
        "title":title
    })

def about(request):
    username = "CiprianoE"
    active = 'about'
    return render(request,"about.html",{
        "username":username,
         "active":active   
    })

def greeting(resquest,username):
    return HttpResponse("<h1> Hello %s </h1>" % username)

def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects,safe=False)
     projects = Project.objects.all()
     active = 'projects'
     return render(request,"projects.html",{
         'projects':projects,
         'active':active
     })

def task(request):
    # task= Task.objects.get(id=id)
    # task =  get_object_or_404(Task, id=id)
    task = Task.objects.all() 
    active = 'task'  
    return render(request,"task.html",{
        'task':task,
        'active':active
    })

def createtask(request):
    """ title = "Create Task" """
    active = 'task'    
    if request.method == 'GET':    
        return render(request, 'createtask.html',{'active':active, 'form':CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'],project_id=1)
        return redirect('task')

def createprojects(request):
    active='projects'
    if request.method == 'GET':
     return render(request,'createprojects.html',{'active':active, 'form':CreateNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')    
    

def detailproject(request, id):
    active='projects'
    #project = Project.objects.get(id=id)
    project =get_object_or_404(Project,id=id) 
    task = Task.objects.filter(project_id = id)
    print(task)    
    return render(request,'detailprojects.html', {'active':active, 'project':project , 'task':task})    