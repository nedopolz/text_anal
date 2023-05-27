from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView

from main.forms import TextAnalyseForm
from main.utils import analyse_text


class IndexPageView(LoginRequiredMixin, FormView):
    template_name = 'main/index.html'
    form_class = TextAnalyseForm

    def form_valid(self, form):
        text = self.request.POST['text']
        topics_rating = analyse_text(text)
        messages.success(self.request, str(topics_rating))

        return redirect('index')
