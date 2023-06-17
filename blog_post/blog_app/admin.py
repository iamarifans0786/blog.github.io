from django.contrib import admin
from blog_app.models import blog_post,comments
# Register your models here.

admin.site.register(blog_post)
 

class modify_comment(admin.ModelAdmin):
    list_display=[
        'post',
        'name',
        'comment_body',
     ] 

admin.site.register(comments,modify_comment)

