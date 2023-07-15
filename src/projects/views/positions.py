from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.decorators import member_required
from users.models import Member

from projects.forms import PositionForm, ApplicantForm
from projects.models import Project, Position, Applicant, ProjectMember

@login_required
@member_required
def position_details(request, pk):
    if pk == None:
        return redirect("not_found")
    
    position = Position.objects.get(pk=pk)
    
    if position == None:
        return redirect("not_found")
    
    context = {}
    context['position'] = position
    context['form'] = ApplicantForm()
    return render(request, "positions/details.html", context)
    

@login_required
@member_required
def position_create(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    if request.method == 'POST':
        form = PositionForm(request.POST or None)
        c = form.save(commit=False)
        c.project = project
        c.save()
        return redirect('project_managers:positions', project.id)
    
    return redirect('project_managers:positions', project.id)

@login_required
@member_required
def position_apply(request, pk):
    if pk == None:
        return redirect("not_found")
    
    position = Position.objects.get(pk=pk)
    
    if position == None:
        return redirect("not_found")
    
    if request.method == "POST":
        form = ApplicantForm(request.POST or None)
        c = form.save(commit=False)
        c.position = position
        c.member = request.user.member
        c.save()
        return redirect("positions:details", position.id)
    return redirect("positions:details", position.id)

@login_required
@member_required
def position_applicants(request, pk):
    if pk == None:
        return redirect("not_found")
    
    position = Position.objects.get(pk=pk)
    
    if position == None:
        return redirect("not_found")
    
    if position.project.manager != request.user.member:
        return redirect("access_denied")
    
    context = {}
    context["position"] = position
    
    return render(request, "positions/applicants.html", context)

@login_required
@member_required
def position_select_applicant(request, pk):
    if pk == None:
        return redirect("not_found")
    
    applicant = Applicant.objects.get(pk=pk)
    
    if applicant == None:
        return redirect("not_found")
    
    position = Position.objects.get(pk=applicant.position.id)
    
    if position == None:
        return redirect("not_found")
    
    if position.project.manager != request.user.member:
        return redirect("access_denied")
    
    position.people_needed = position.people_needed - 1
    position.positions_filled = position.positions_filled + 1
    position.save()
    
    ProjectMember.objects.create(role="Staff", position=position.title, member=applicant.member, project=applicant.position.project)
    
    applicant.delete()
    
    return redirect("positions:applicants", position.id)

