from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from projects.models import Project, Position, Applicant

@login_required
def position_details(request, pk):
    if pk == None or pk == 0:
        return redirect("not_found")
    
    position = Position.objects.get(pk=pk)
    
    if position == None:
        return redirect("not_found")
    
    return render(request, "positions/details.html", { 'position': position })
