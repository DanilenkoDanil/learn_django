from django.contrib import admin
from second.models import Author
from second.models import Post
from second.models import Category


@admin.register(Author)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Post)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'date','like', 'dislike', 'donate')

@admin.register(Category)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', ) 