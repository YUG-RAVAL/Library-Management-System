import attr
from django import forms
from .models import lib

class BookRegistraion(forms.ModelForm):
   class Meta:
       model = lib
       fields = ['name','description']
       widgets = {
           'name':forms.TextInput(attrs={'class':'form-control'}),
           'description':forms.TextInput(attrs={'class':'form-control'}),
       }
