from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import Member

def profile_list(request):
    members = Member.objects.all()
    context = {}
    context["members"] = members
    
    return render(request, "profiles/list.html", context)

def profile(request, slug):
    if slug == None or slug == "":
        return redirect("not_found")
    
    member = Member.objects.get(slug=slug)
    
    if member == None:
        return render("not_found")
    
    context = {}
    context["member"] = member
    return render(request, "profiles/profile.html", context)

def profile_about(request, slug):
    if slug == None or slug == "":
        return redirect("not_found")
    
    member = Member.objects.get(slug=slug)
    
    if member == None:
        return render("not_found")
    
    context = {}
    context["member"] = member
    return render(request, "profiles/about.html", context)