from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from events.forms import EventForm
from events.models import Event

def event_details(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, "events/details.html", {"event": event})
