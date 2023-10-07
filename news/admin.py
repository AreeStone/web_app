from django.contrib import admin

from .models import Articles, Comment

admin.site.register(Articles)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['new', 'author', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['author' 'body']