from django.contrib import admin

from blog_site.models.author import Author
from blog_site.models.post import Post

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
