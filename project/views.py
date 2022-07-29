from django.shortcuts import render
from project.models import Projects

# Create your views here.
def dashboard(request):
    return render(request, 'project/accueil.html')

def project_index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project_index.html', context)

def project_detail(request, pk):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project/project_detail.html', context)


