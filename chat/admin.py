from django.contrib import admin
from .models import Message, Chat

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    fields = ('author','created_at','text','receiver','chat')
    list_display = ('author','created_at','text','receiver')
    search_fields = ('text',)

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
