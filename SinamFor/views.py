
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .forms import QuoteRequestForm
from blog.models import Service

def home(request):
    is_home_page=True
    return render(request,'pages/home.html', {'is_home_page':is_home_page})


def services(request):
    is_home_page = False
    return render(request,'pages/services.html', {'is_home_page':is_home_page})



def contact(request):
    is_home_page = False
    return render(request,'pages/contact.html',{'is_home_page':is_home_page})


def about(request):
    is_home_page = False
    return render(request,'pages/about.html', {'is_home_page':is_home_page})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def quote_request_view(request):
    services=Service.objects.all()
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your quote request has been sent successfully!')
            return redirect('request')
    else:
        form = QuoteRequestForm()

    return render(request, 'pages/request.html', {'form': form, 'services':services})
