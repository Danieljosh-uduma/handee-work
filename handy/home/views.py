from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home/post.html', context)

def post_view(request, pk):
    post = Post.objects.get(head=pk)
    context = {'post': post}
    return render(request, 'home/post_view.html', context)