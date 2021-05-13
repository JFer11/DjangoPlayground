from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Thread

"""
# This is another way to craft the View, but it is not necessary since through request.user.threads.all() we can access
# every thread that belongs to logged user.
@method_decorator(login_required, name='dispatch')
class ThreadList(ListView):
    model = Thread

    def get_queryset(self):
        queryset = super(ThreadList, self).get_queryset()
        return queryset.filter(users=self.request.user)
"""


class ThreadList(TemplateView):
    template_name = 'messenger/thread_list.html'


@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self, queryset=None):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

