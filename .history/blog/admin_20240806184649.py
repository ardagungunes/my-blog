from django.contrib import admin
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = 

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)