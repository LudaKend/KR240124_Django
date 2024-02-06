from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'head', 'preview', 'data_create', 'is_published', 'views_count')
    list_filter = ('data_create', 'is_published',)
    search_fields = ('preview',)
