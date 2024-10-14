from django.shortcuts import render,HttpResponse
from api.models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm 


def index(request):
 return render(request,"index.html")

def createpost(request):
    form=PostForm()

    #save the data to database
    if request.method=="POST":
       form=PostForm(request.POST)
   

       if form.is_valid():
          form.save()
          return HttpResponse("Post created Successful!")

    return render(request,"create-post.html",{"form":form})


def postlist(request ):
  Postlist=Post.objects.all()

  return render(request,"post-list.html",{"Postlist":Postlist})


def postdetails(request,slug):
  post=Post.objects.filter(slug=slug)

  return render(request,"postdetails.html",{"post":post})


