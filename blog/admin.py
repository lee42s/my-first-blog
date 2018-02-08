from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','author','title','published_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','author','text','approved_comment')

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)