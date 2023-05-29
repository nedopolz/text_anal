from django.urls import path

from main.views import analyze_text

app_name = 'analyze'

urlpatterns = [
    path('analyze/', analyze_text)
]
