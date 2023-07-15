from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from events.models import Event, Attendee
from projects.forms import ProjectForm
from projects.models import Action
from small_groups.forms import SmallGroupForm
from small_groups.models import SmallGroup, GroupMember
from users.decorators import member_required
from users.models import Member

@login_required
@member_required
def member_detail(request, pk):
    if pk == None:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    return render(request, "members/detail.html")

@login_required
@member_required
def member_applications(request, pk):
    if pk == None:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    return render(request, "members/applications.html", {'member': member})

@login_required
@member_required
def member_projects(request, pk):
    if pk == None:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    form = ProjectForm()
    context = {}
    context["form"] = form
    context["member"] = member
    
    return render(request, "members/projects.html", context)

@login_required
@member_required
def member_groups(request, pk):
    if pk == None:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    context = {}
    context["member"] = member
    context["form"] = SmallGroupForm()
    
    return render(request, "members/groups.html", context)

@login_required
@member_required
def member_group_create(request, pk):
    if pk == None:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    if request.method == 'POST':
        form = SmallGroupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.creator = member
            c.save()
            GroupMember.objects.create(member=member, small_group=c)
            return redirect("members:groups", member.id)
    return redirect("members:groups", member.id)

@login_required
@member_required
def member_calendar(request, pk):
    if pk == None:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    events = Attendee.objects.filter(member=member)
    
    context = {}
    context["events"] = events
    
    return render(request, "members/calendar.html", context)

# @login_required
# @member_required
# def member_assignments(request, pk):
#     if pk == None:
#         return redirect("not_found")
    
#     member = Member.objects.get(pk=pk)
    
#     if member == None:
#         return redirect("not_found")
    
#     if member.identity != request.user:
#         return redirect("access_denied")
    
#     assignments = Action.objects.filter(assignees__contains=[{"id":request.user.member.id}])
    
#     context = {}
#     context["assignments"] = assignments
    
#     return render(request, "members/assignments.html", context)

# @login_required
# @member_required
# def member_assignment_details(request, action_pk):
#     if action_pk == None:
#         return redirect("not_found")
    
#     action = Action.objects.get(pk=action_pk)
    
#     if action == None:
#         return redirect("not_found")
    
#     for assignee in action.assignees:
#         if request.user.member.id != assignee['id']:
#             return redirect("access_denied")
    
#     context = {}
#     context['action'] = action
    
#     return render(request, "members/assignment_details.html", context)