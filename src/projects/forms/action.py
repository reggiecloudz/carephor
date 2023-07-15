from django import forms

from projects.models import Action

class ActionForm(forms.ModelForm):
    label = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    start_date = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M', required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    deadline = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M', required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    
    class Meta:
        model = Action
        fields = ("label", "details", "start_date", "deadline")

class ActionCompletionForm(forms.ModelForm):
    results = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    
    class Meta:
        model = Action
        fields = ("results",)
