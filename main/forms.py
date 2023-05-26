from django import forms


class TextAnalyseForm(forms.Form):
    text = forms.CharField(label="Текст для анализа", max_length=30000, required=False)
