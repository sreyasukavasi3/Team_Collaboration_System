from django.contrib import admin
from .models import DirectMessage,GroupMessage

admin.site.register(DirectMessage)
admin.site.register(GroupMessage)