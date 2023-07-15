from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.decorators import member_required
from events.forms import EventForm
from events.models import Event

@login_required
@member_required
def event_info(request, pk):
    if pk == None:
        return redirect('not_found')

    event = Event.objects.get(pk = pk)
    
    if event == None:
        return redirect('not_found')
    
    context ={}
    context['event'] = event
    return render(request, 'events/info.html', context)

@login_required
def event_details(request, id):
    if id == None:
        return redirect('not_found')

    event = Event.objects.get(id = id)
    
    if event == None:
        return redirect('not_found')
    
    context ={}
    context['event'] = Event.objects.get(id = id)
    return render(request, 'events/detail_view.html', context)

@login_required
def event_update(request, id):
    if id == None:
        return redirect('not_found')

    event = Event.objects.get(id = id)
    
    if event == None:
        return redirect('not_found')
    
    context ={}
    context['save_context']= 'Update'
    
    form = EventForm(request.POST or None, request.FILES or None, instance = event)
    
    if form.is_valid():
        form.save()
        return redirect('events:event_detail', id)

    context['form'] = form
 
    return render(request, 'events/save_view.html', context)

@login_required
def event_delete(request, id):
    if id == None or id == 0:
        return redirect('not_found')

    event = Event.objects.get(id = id)
    
    if event == None:
        return redirect('not_found')
    
    context ={}
 
    if request.method == 'POST':
        event.delete()
        return redirect('home')
 
    return render(request, 'events/delete_view.html', context)