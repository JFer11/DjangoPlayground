from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PageForm
from .models import Page

"""
# DEPRECATED, just to show how to extends features with inheritance.
# HOW IT WAS USED: It was inherited from a CRUD view to add staff permissions. 
class StaffRequiredMixin:
    # Requires that logged user must be a staff member.

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
"""

"""
# OLD VIEW FUNCTION
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})
"""


class PageListView(ListView):
    model = Page


"""
OLD VIEW FUNCTION
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})
"""


class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
