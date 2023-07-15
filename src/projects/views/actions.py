from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from events.models import Event
from users.decorators import member_required
from projects.forms import ActionForm, ActionCompletionForm
from projects.models import Action, Project, ProjectMember

@login_required
@member_required
def action_create(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    if request.method == 'POST':
        form = ActionForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.project = project
            c.save()
            '''
            TODO: Add event
            '''
            Event.objects.create(
                owner=project, 
                name=f"{project.name}: {c.label}",
                details=c.details,
                venue="Not Specified",
                location="Not Specified",
                start_time=c.start_date,
                end_time=c.deadline,
            )
            return redirect('project_managers:actions', project.id)
    return redirect('project_managers:actions', project.id)

@login_required
@member_required
def action_detail(request, pk):
    if pk == None:
        return redirect('not_found')

    action = Action.objects.get(pk=pk)
    
    if action == None:
        return redirect('not_found')
    
    context ={}
    context['action'] = action
    context['form'] = ActionForm(instance=action)
    context['cform'] = ActionCompletionForm(instance=action)
    context['staff'] = ProjectMember.objects.filter(project=action.project, role="Staff")
    return render(request, 'actions/details.html', context)

@login_required
@member_required
def action_assign(request, pk):
    if pk == None:
        return redirect('not_found')

    action = Action.objects.get(pk=pk)
    
    if action == None:
        return redirect('not_found')
    
    if request.method == 'POST':
        event = Event.objects.get(owner_id=action.project.pk, name=f"{action.project.name}: {action.label}")
        assignees = request.POST.getlist('assignee')
        for assignee_id in assignees:
            pm = ProjectMember.objects.get(project=action.project, member__pk=assignee_id)
            assignee = {
                "id": pm.member.pk,
                "name": pm.member.identity.name,
                "photo": pm.member.identity.photo.url,
                "position": pm.position,
                "slug": pm.member.slug
            }
            action.assignees.append(assignee)
            event.attendees.add(pm.member)
        action.save()
        event.save()
        return redirect("actions:details", action.id)

@login_required
@member_required
def action_start(request, pk):
    if pk == None:
        return redirect('not_found')

    action = Action.objects.get(pk=pk)
    
    if action == None:
        return redirect('not_found')
    
    if request.user != action.project.manager.identity:
        return redirect('access_denied')
        
    action.clocked_start = datetime.now()
    action.save()
    return redirect("actions:details", action.id)

@login_required
@member_required
def action_complete(request, pk):
    if pk == None:
        return redirect('not_found')

    action = Action.objects.get(pk=pk)
    
    if action == None:
        return redirect('not_found')
    
    if request.user != action.project.manager.identity:
        return redirect('access_denied')
    
    if request.method == 'POST':
        form = ActionCompletionForm(request.POST or None, instance=action)
        if form.is_valid():
            c = form.save(commit=False)
            c.completed_at = datetime.now()
            c.complete = True 
            c.save()
            return redirect("actions:details", action.id)
    return redirect("actions:details", action.id)

@login_required
@member_required
def action_update(request, id):
    if id == None or id == 0:
        return redirect('not_found')

    action = Action.objects.get(id = id)
    
    if action == None:
        return redirect('not_found')
    
    context ={}
    context['save_context']= 'Update'
    
    form = ActionForm(request.POST or None, request.FILES or None, instance = action)
    
    if form.is_valid():
        form.save()
        return redirect('projects:action_detail', id)

    context['form'] = form
 
    return render(request, 'actions/save_view.html', context)

@login_required
@member_required
def action_delete(request, id):
    if id == None or id == 0:
        return redirect('not_found')

    action = Action.objects.get(id = id)
    
    if action == None:
        return redirect('not_found')
    
    context ={}
 
    if request.method == 'POST':
        action.delete()
        return redirect('home')
 
    return render(request, 'actions/delete_view.html', context)