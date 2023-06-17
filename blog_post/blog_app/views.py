from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from blog_app.models import blog_post,comments

# Create your views here.

def default(request):
    return HttpResponse(" <H1> Project Running </H1> ")

def home(request):
    items=blog_post.objects.all()
    search_element=request.GET.get("search","")
    if search_element:
       items=blog_post.objects.filter(title__icontains=search_element)
       return render(request,'blog_app_temp/home.html',{
        "item":items
    }) 
    return render(request,'blog_app_temp/home.html',{
        "item":items
    })


def explore(request,id):
    comment_body = name = None
    if request.method == "POST":
        comment_body=request.POST.get("comment_body")
        name=request.POST.get("name")
        
    items=blog_post.objects.get(id=id)
    if comment_body and name:
        data=comments(post=items,comment_body=comment_body,name=name)
        data.save()

    all_comment=comments.objects.filter(post=items)  

    return render(request,'blog_app_temp/explore.html',{
        "item":items,
        'all_comment':all_comment
    })

def get_one(request,id):
    
    item=blog_post.objects.get(id=id)
    return HttpResponseRedirect(reverse('explore_content'))

