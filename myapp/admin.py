from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Post, Like, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('title', )
    ordering = ('-created_at', )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_display_links = ('post', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
