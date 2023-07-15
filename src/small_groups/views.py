from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from classifications.models import Cause, Tag
from small_groups.forms import SmallGroupForm
from small_groups.models import SmallGroup
from posts.forms import PostPhotoForm, PostTextForm
from users.decorators import member_required
from users.models import Member


def group_profile(request, slug):
    group = get_object_or_404(SmallGroup, slug=slug)
    
    context = {}
    context["group"] = group
    context["post_photo_form"] = PostPhotoForm()
    return render(request, "small_groups/profile.html", context)

@login_required
@member_required
def group_details(request, pk):
    group = get_object_or_404(SmallGroup, pk=pk)
    
    if group.creator != request.user.member:
        return redirect("access_denied")
    
    context = {
        "group": group,
        "form": SmallGroupForm(instance=group),
        "tags": Tag.objects.filter(cause=group.cause)
    }
    return render(request, "small_groups/details.html", context)

def group_events(request, pk):
    group = get_object_or_404(SmallGroup, pk=pk)
    context = {
        "group": group
    }
    return render(request, "small_groups/events.html", context)

def group_members(request, pk):
    group = get_object_or_404(SmallGroup, pk=pk)
    context = {
        "group": group
    }
    return render(request, "small_groups/members.html", context)

@login_required
@member_required
def group_join(request, pk):
    group = get_object_or_404(SmallGroup, pk=pk)
    
    group.members.add(request.user.member)
    group.save()
    return redirect("groups:profile", group.id)
