from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from campaigns.forms import CampaignForm
from campaigns.models import Campaign

@login_required
def create_view(request):
    context ={}
    context['save_context'] = 'Create'
    
    if request.method == 'POST':
        form = CampaignForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.manager = request.user.member
            c.save()
            return redirect("members:campaigns", request.user.member.pk)
    
    return redirect("members:campaigns", request.user.member.pk)

def list_view(request):
    context ={}
    context['campaigns'] = Campaign.objects.all()
    return render(request, 'campaigns/list_view.html', context)

def campaign_details(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/details.html', context)

def campaign_news(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/news.html', context)

def campaign_events(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/events.html', context)

def campaign_members(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/members.html', context)

def campaign_positions(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/positions.html', context)

def campaign_photos(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/photos.html', context)

def campaign_videos(request, pk):
    if pk == None:
        return redirect('not_found')

    campaign = Campaign.objects.get(pk=pk)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['campaign'] = campaign
    return render(request, 'campaigns/videos.html', context)

@login_required
def update_view(request, id):
    if id == None or id == 0:
        return redirect('not_found')

    campaign = Campaign.objects.get(id = id)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
    context['save_context']= 'Update'
    
    form = CampaignForm(request.POST or None, request.FILES or None, instance = campaign)
    
    if form.is_valid():
        form.save()
        return redirect('campaigns:campaign_detail', id)

    context['form'] = form
 
    return render(request, 'campaigns/save_view.html', context)

@login_required
def delete_view(request, id):
    if id == None or id == 0:
        return redirect('not_found')

    campaign = Campaign.objects.get(id = id)
    
    if campaign == None:
        return redirect('not_found')
    
    context ={}
 
    if request.method == 'POST':
        campaign.delete()
        return redirect('home')
 
    return render(request, 'campaigns/delete_view.html', context)