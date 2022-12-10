from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Pull
from webapp.forms import PullForm


# Create your views here.


class IndexView(ListView):
    template_name = 'pull/index.html'
    model = Pull
    context_object_name = 'pull'
    paginate_by = 5


class PullView(DetailView):
    template_name = 'pull/info.html'
    model = Pull
    order_by = 'option'


class PullAddView(CreateView):
    template_name = 'pull/add.html'
    model = Pull
    form_class = PullForm

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})


class PullUpdateView(UpdateView):
    model = Pull
    template_name = 'pull/update.html'
    form_class = PullForm
    context_key = 'pull'

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})


class PullDeleteView(DeleteView):
    template_name = 'pull/delete.html'
    model = Pull
    context_object_name = 'pull'
    success_url = reverse_lazy('index')
