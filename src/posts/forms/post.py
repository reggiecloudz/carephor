from django import forms

from posts.models import Post

class PostTextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4, 
        'class': 'form-control pe-4 fs-3 lh-1 border-0',
        'placeholder': 'Share your thoughts...',
    }))

class PostPhotoForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4, 
        'class': 'form-control pe-4 fs-3 lh-1 border-0',
        'placeholder': 'Share your thoughts...',
    }))
    images = forms.ImageField(max_length=144, required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    

class PostVideoForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 2, 
        'class': 'form-control pe-4 fs-3 lh-1 border-0',
        'placeholder': 'Share your thoughts...',
    }))