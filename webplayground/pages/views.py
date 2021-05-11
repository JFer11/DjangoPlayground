from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PageForm
from .models import Page


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


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
