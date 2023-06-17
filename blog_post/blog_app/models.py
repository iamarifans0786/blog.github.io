from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class blog_post(models.Model):
    title=models.CharField(max_length=500)
    sub_title=models.CharField(max_length=500)
    blog_image=models.ImageField(upload_to="blog_img")
    body_content=HTMLField()
    publish_date=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.title

class comments(models.Model):
    post=models.ForeignKey(blog_post,on_delete=models.CASCADE)
    comment_body=models.TextField()
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.comment_body
    
 
