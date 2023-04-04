from django.contrib import admin
from snippets.models import Snippet

@admin.register(Snippet)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id',)
# Register your models here.
