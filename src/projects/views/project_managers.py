from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from events.forms import EventForm
from events.models import Event
from users.decorators import member_required
from users.models import Member

from projects.forms import PositionForm, ActionForm, ExpenditureForm, ProposalForm, ProjectForm
from projects.models import Project, Position, Applicant, ProjectMember, Proposal

@login_required
@member_required
def project_manager_about(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    context = {}
    context['project'] = project
    context['project_form'] = ProjectForm(instance=project)
    context['proposal_form'] = ProposalForm(instance=project.proposal)
    
    return render(request, 'project_managers/about.html', context)

@login_required
@member_required
def project_manager_actions(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    context = {}
    context['project'] = project
    context['form'] = ActionForm()
    
    return render(request, 'project_managers/actions.html', context)

@login_required
@member_required
def project_manager_expenditures(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    context = {}
    context['project'] = project
    context['form'] = ExpenditureForm()
    
    return render(request, 'project_managers/expenditures.html', context)

@login_required
@member_required
def project_manager_positions(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    context = {}
    context['form'] = PositionForm()
    context['project'] = project
    
    return render(request, 'project_managers/positions.html', context)

@login_required
@member_required
def project_manager_members(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    members = ProjectMember.objects.filter(project=project)
    
    context = {}
    context['project'] = project
    context['members'] = members
    
    return render(request, 'project_managers/members.html', context)

@login_required
@member_required
def project_manager_events(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    context = {}
    context['project'] = project
    context['form'] = EventForm()
    return render(request, 'project_managers/events.html', context)

@login_required
@member_required
def project_manager_add_events(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    if request.method == 'POST':
        form = EventForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.owner = project
            c.save()
            return redirect("project_managers:events", project.id)
    return redirect("project_managers:events", project.id)
