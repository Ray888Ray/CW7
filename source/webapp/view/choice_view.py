from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from webapp.models import Choice, Pull
from django.views.generic import CreateView, DeleteView, UpdateView
from webapp.forms import ChoiceForm


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/choice_delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse_lazy('info', kwargs={'pk': self.object.pull.pk})


class ChoiceAddView(CreateView):
    template_name = 'choice/choice_add.html'
    model = Choice
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pull.pk})

    def form_valid(self, form):
        pull = get_object_or_404(Pull, pk=self.kwargs.get('pk'))
        form.instance.pull = pull
        return super().form_valid(form)


class ChoiceUpdatedView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pull.pk})
