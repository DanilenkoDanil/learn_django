from django.contrib import admin
from steam.models import Mail, Account, Game

# Register your models here.

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('login', 'password')
    search_field = ['login', 'password']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'coast', 'description', 'mail')
    search_field = ['login', 'password', 'coast', 'description', 'mail']

@admin.register(Game)
class GamegAdmin(admin.ModelAdmin):
    list_display = ('name', 'coast', 'version')
    search_field = ['name', 'coast', 'version']