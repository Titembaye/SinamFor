from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('contact-us/', views.contact_view, name='contact_us'),
    path('about/', views.about, name='about'),
    path('request/', views.quote_request_view, name='request')

]
