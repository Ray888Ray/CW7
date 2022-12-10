from webapp.models import Answer, Choice
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from webapp.forms import AnswerForm


class AnswerView(TemplateView):
    template_name = 'answer/answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer'] = Answer.objects.all()
        form = AnswerForm(self.request.POST)
        context["form"] = form
        return context