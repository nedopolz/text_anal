from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.forms import TextAnalyseForm
from main.serializers import TextInputSerializer
from main.utils import analyse_text


class IndexPageView(LoginRequiredMixin, FormView):
    template_name = 'main/index.html'
    form_class = TextAnalyseForm

    def form_valid(self, form):
        text = self.request.POST['text']
        topics_rating = analyse_text(text)
        messages.success(self.request, str(topics_rating))

        return redirect('index')


@api_view(['POST'])
def analyze_text(request):
    serializer = TextInputSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    result = serializer.save()
    return Response(data=result)
