from django.shortcuts import render, redirect

from campaigns.models import Campaign

def home(request):
    # if request.user.is_authenticated:
    #     return redirect("members:member_detail", request.user.member.id)
    
    template_name='pages/home.html'
    context = {}
    context["campaigns"] = Campaign.objects.all()
    return render(request, template_name, context)

def not_found(request):
    template_name = "pages/not_found.html"
    return render(request, template_name)

def access_denied(request):
    template_name = "pages/access_denied.html"
    return render(request, template_name)