from django.contrib import admin
from .models import Contact, Service, QuoteRequest
# Register your models here.
admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(QuoteRequest)
