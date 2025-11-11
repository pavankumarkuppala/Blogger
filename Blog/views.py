from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", {"blogs" : blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {"form":form})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog' : blog})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user = request.user)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES, instance=blog)
        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form' : form})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blog_delete.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {"form" : form})

@login_required
def my_blogs(request):
    blogs = Blog.objects.filter(user=request.user)
    return render(request, 'index.html', {'blogs' : blogs})

def search_blog(request):
    if request.method == 'POST':
        keyword = request.POST.get('search')
        blogs = Blog.objects.filter(title__icontains=keyword)
    else:
        blogs = None
    return render(request, 'index.html', {'blogs':blogs})