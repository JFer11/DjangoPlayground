from .models import Page
from django import forms


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titulo'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Orden'
            })
        }
        """
        labels = {
            'title': '', 'order': ''  # This will remove the title above the form field.
        }
        """
