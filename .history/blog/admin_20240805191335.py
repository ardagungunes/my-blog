from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.register(Tag)