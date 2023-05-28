from django.urls import path

from analyze.views import analyze_text

app_name = 'analyze'

urlpatterns = [
    path('analyze/', analyze_text)
]
