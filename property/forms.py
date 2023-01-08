from django import forms
from .models import proberty_book
class ProbertyBookForm(forms.ModelForm):
    class Meta:
        model=proberty_book
        fields=['date_from','date_to','guest','children']

    
