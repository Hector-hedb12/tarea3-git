from django import forms

class ConsultForm(forms.Form):
    url_text = forms.CharField(max_length=400)