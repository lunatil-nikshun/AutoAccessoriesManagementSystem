from django import forms
from .models import Accessories

class PartForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'detail', 'price', 'image', 'tags']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'detail' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
            'tags' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }
