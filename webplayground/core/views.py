from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        # Add a variable to context dict, to add some context to the template.
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        # Here we could inject some context as we did in function based views.
        return render(request, "core/home.html")


class SamplePageView(TemplateView):

    template_name = "core/sample.html"
