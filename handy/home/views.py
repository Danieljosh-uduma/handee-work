from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home/post.html', context)

def post_view(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'home/post_view.html', context)

def create_post(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form': form}
    return render(request, 'home/create_post.html', context)

def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
        
    context = {'form': form}
    return render(request, 'home/create_post.html', context)

def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'obj': post}
    return render(request, 'home/delete.html', context)
    