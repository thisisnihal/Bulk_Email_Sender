# forms.py
from django import forms

class EmailForm(forms.Form):
    email_content = forms.CharField(widget=forms.Textarea(attrs={'id': 'summernote'}))
