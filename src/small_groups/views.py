from django.shortcuts import render, redirect

from small_groups.models import SmallGroup, GroupMember

def group_details(request, pk):
    group = SmallGroup.objects.get(pk=pk)
    context = {
        "group": group
    }
    return render(request, "small_groups/details.html", context)

def group_events(request, pk):
    group = SmallGroup.objects.get(pk=pk)
    context = {
        "group": group
    }
    return render(request, "small_groups/events.html", context)

def group_members(request, pk):
    group = SmallGroup.objects.get(pk=pk)
    context = {
        "group": group
    }
    return render(request, "small_groups/members.html", context)
