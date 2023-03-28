from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
