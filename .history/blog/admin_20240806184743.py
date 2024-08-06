from django.contrib import admin
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date",)
    list_display = ("title", "date", "date",)

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)