from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from projects.forms import ProjectForm
from users.models import Member

@login_required
def member_detail(request, pk):
    if pk == None or pk == 0:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    return render(request, "members/detail.html")

@login_required
def member_applications(request, pk):
    if pk == None or pk == 0:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    return render(request, "members/applications.html", {'member': member})

@login_required
def member_projects(request, pk):
    if pk == None or pk == 0:
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
def member_groups(request, pk):
    if pk == None or pk == 0:
        return redirect("not_found")
    
    member = Member.objects.get(pk=pk)
    
    if member == None:
        return redirect("not_found")
    
    if member.identity != request.user:
        return redirect("access_denied")
    
    context = {}
    context["member"] = member
    
    return render(request, "members/groups.html", context)

