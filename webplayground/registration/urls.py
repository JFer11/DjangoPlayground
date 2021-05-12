from django.urls import path
from .views import UserSignUp, ProfileUpdate


urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile')
]
