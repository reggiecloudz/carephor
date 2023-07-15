from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.decorators import member_required
from projects.forms import ProjectForm, PositionForm
from projects.models import Project, ProjectMember

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
    
    context = {}
    
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

def project_goals(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    context ={}
    context['project'] = project
    return render(request, 'projects/goals.html', context)

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
    
    
    project_members = ProjectMember.objects.filter(project__id=project.id)
    
    context ={}
    context['project'] = project
    context['project_members'] = project_members
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

@login_required
@member_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            c = form.save(commit=False)
            # additional data
            c.manager = request.user.member
            c.save()
            return redirect("members:projects", request.user.member.id)
    return redirect("members:projects", request.user.member.id)

@login_required
@member_required
def project_join(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if request.user.member in project.members.all():
        return redirect("projects:details", project.id)
    
    ProjectMember.objects.create(position='Supporter', member=request.user.member, project=project)
    
    return redirect("projects:details", project.id)
