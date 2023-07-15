from django import forms

from projects.models import Applicant

class ApplicantForm(forms.ModelForm):
    qualifications = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    
    class Meta:
        model = Applicant
        fields = ('qualifications',)