from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdimin(admin.ModelAdmin):
    pass
