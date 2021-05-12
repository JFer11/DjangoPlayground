from django.urls import reverse_lazy
from django import forms
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from registration.forms import UserCreationFromWithEmail, ProfileForm, EmailForm
from .models import Profile


class UserSignUp(CreateView):
    form_class = UserCreationFromWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(UserSignUp, self).get_form()
        # Modify the form in execution time.
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


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # Get the object that we are going to modify
        # Read how django handles UpdateViews.
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modify the form in execution time.
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Email'
        })
        return form
