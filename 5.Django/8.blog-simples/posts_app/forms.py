from django import forms
from .models import Posts

class PostsForms(forms.ModelForm):
    class Meta:
        model = Posts # model de criado em models
        fields = ['title', 'descriptions', 'image'] # campos do model
