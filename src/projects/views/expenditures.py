from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.decorators import member_required
from projects.forms import ExpenditureForm
from projects.models import Expenditure, Project

@login_required
@member_required
def expenditure_create(request, pk):
    if pk == None:
        return redirect('not_found')

    project = Project.objects.get(pk=pk)
    
    if project == None:
        return redirect('not_found')
    
    if project.manager != request.user.member:
        return redirect('access_denied')
    
    if request.method == 'POST':
        form = ExpenditureForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.project = project
            c.save()
            return redirect("project_managers:expenditures", project.id)
    return redirect("project_managers:expenditures", project.id)

@login_required
def expenditure_detail(request, id):
    if id == None:
        return redirect('not_found')

    expenditure = Expenditure.objects.get(id = id)
    
    if expenditure == None:
        return redirect('not_found')
    
    context ={}
    context['expenditure'] = expenditure
    return render(request, 'expenditures/detail_view.html', context)

@login_required
def expenditure_update(request, id):
    if id == None:
        return redirect('not_found')

    expenditure = Expenditure.objects.get(id = id)
    
    if expenditure == None:
        return redirect('not_found')
    
    context ={}
    context['save_context']= 'Update'
    
    form = ExpenditureForm(request.POST or None, request.FILES or None, instance = expenditure)
    
    if form.is_valid():
        form.save()
        return redirect('projects:expenditure_detail', id)

    context['form'] = ExpenditureForm(instance=expenditure)
 
    return render(request, 'expenditures/save_view.html', context)

@login_required
def expenditure_delete(request, id):
    if id == None:
        return redirect('not_found')

    expenditure = Expenditure.objects.get(id = id)
    
    if expenditure == None:
        return redirect('not_found')
    
    context ={}
 
    if request.method == 'POST':
        expenditure.delete()
        return redirect('home')
 
    return render(request, 'expenditures/delete_view.html', context)