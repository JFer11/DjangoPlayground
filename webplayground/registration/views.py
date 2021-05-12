from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django import forms
from django.views.generic import CreateView
from registration.forms import UserCreationFromWithEmail


class UserSignUp(CreateView):
    form_class = UserCreationFromWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(UserSignUp, self).get_form()
        # Modify in execution time the form.
        form.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Nombre del usuario'
        })
        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Contraseña'
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Repite la contraseña'
        })
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Dirección de email'
        })
        # We can do this: "form.fields['username'].label = '' ", however, lets modify the css in signup.html directly.
        return form
