from django import forms

class ContactForm (forms.Form):
    name = forms.CharField(max_length=30)
    job = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    tel = forms.CharField(max_length=9)
    message = forms.CharField(max_length=2000, widget=forms.Textarea, required=True)