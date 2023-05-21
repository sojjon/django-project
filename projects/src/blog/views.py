from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def home_view(request):
    blog = Blog.objects.all().first
    featured_post = Post.objects.filter(featured=True)[:4]
    story_post = Post.objects.filter(featured=False)
    context = {'blog':blog,'featured_post':featured_post,'story_post':story_post}
    return render(request,'blog/index.html',context)


def single_view(request,slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post':post}
    return render(request,'blog/post.html', context)