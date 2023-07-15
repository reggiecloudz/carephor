from django import forms

from projects.models import Expenditure

class ExpenditureForm(forms.ModelForm):
    item = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    purpose = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    cost = forms.DecimalField(max_value=500000, min_value=1, max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Expenditure
        fields = ("item", "purpose", "cost")
