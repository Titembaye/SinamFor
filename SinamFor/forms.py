from django import forms
from blog.models import Contact, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}),
        }

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': 'Your Name', 'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0', 'placeholder': 'Your Email', 'style': 'height: 55px;'}),
            'service': forms.Select(attrs={'class': 'form-select bg-light border-0', 'style': 'height: 55px;'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-light border-0', 'rows': 3, 'placeholder': 'Message'}),
        }
