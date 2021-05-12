from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserCreationFromWithEmail(UserCreationForm):
    # We are extending the functionality of UserCreationForm, and we have to highlight the fact that a field called
    # email already existed in the user model. Here we are just adding a form field. That is the reason why we could
    # add 'email' in the fields and everything works.
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, pruebe con otro.")
        return email
