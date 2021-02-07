from django.shortcuts import render, redirect
from .models import ClassProject, Project
from .forms import ClassForm, ProjectForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def projectList(request):
    projects = Project.objects.all()
    return render(request, "project-list.html", { 'projects':projects })

def projectCreate(request):  
    if request.method == "POST":  
        form = ProjectForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('project-list')  
            except:  
                pass  
    else:  
        form = ProjectForm()  
    return render(request,'project-create.html',{'form':form})  

def projectEdit(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(initial={'name_project':project.name_project,'list_name':project.list_name,'professor_name':project.professor_name,'detail_project':project.detail_project})
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/project-list')
            except Exception as e:
                pass
    return render(request, 'project-edit.html',{'form':form})

def projectDelete(request, id):
    project = Project.objects.get(id=id)
    try:
        project.delete()
    except:
        pass
    return redirect('project-list')