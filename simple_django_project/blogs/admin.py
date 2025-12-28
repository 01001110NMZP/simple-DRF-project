from django.contrib import admin
from .models import Blog

# registering the model in the admin site for easier maintenance
admin.site.register(Blog)
