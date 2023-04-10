from django import forms

from events.models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}))
    venue = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(max_length=144, required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    start_time = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    end_time = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    num_of_attendees = forms.IntegerField(max_value=10000, min_value=1, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Event
        fields = (
            "name", 
            "details", 
            "venue", 
            "location",
            "photo",
            "start_time",
            "end_time",
            "num_of_attendees",
        )
