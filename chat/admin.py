from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
  # fields = ('created_at',)
    list_display = ('author','created_at','text','receiver')
    search_fields = ('text',)

admin.site.register(Message, MessageAdmin)
