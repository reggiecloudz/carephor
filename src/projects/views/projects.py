from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from projects.forms import ProjectForm
from projects.models import Project

def project_list(request):
    context = {}
    context['projects'] = Project.objects.all()
    return render(request, 'projects/list.html', context)

def project_details(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    
    if request.user.is_authenticated:
        if request.user.is_member and project.manager == request.user.member:
            context["form"] = ProjectForm(instance=project)
    
    context['project'] = project
    return render(request, 'projects/details.html', context)

def project_news(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/news.html', context)

def project_events(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/events.html', context)

def project_members(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/members.html', context)

def project_positions(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/positions.html', context)

def project_photos(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/photos.html', context)

def project_videos(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/videos.html', context)
