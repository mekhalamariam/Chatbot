from django.contrib import admin
from .models import Reply, UserMessage

# Register your models here.
admin.site.register(Reply)
admin.site.register(UserMessage)
