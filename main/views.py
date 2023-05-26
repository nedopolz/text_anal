from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView

from main.forms import TextAnalyseForm


class IndexPageView(LoginRequiredMixin, FormView):
    template_name = 'main/index.html'
    form_class = TextAnalyseForm

    def form_valid(self, form):
        # TODO весь анализ тут
        text = self.request
        messages.success(self.request, "Это 100% текст про бипки мамой клянусь")

        return redirect('index')
