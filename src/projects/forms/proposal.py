from django import forms

from projects.models import Proposal

class ProposalForm(forms.ModelForm):
    problem = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    goal = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    beneficiaries = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    importance = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    solution = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    execution = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    
    class Meta:
        model = Proposal
        fields = (
            "problem", 
            "goal", 
            "beneficiaries", 
            "importance",
            "solution",
            "execution",
        )
