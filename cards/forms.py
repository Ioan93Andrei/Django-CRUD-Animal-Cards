from django import forms
from .models import Card, Blog

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['picture', 'name', 'description']

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['text']