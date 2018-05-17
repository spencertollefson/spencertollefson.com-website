from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.db.models import Q


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def journal_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/journal_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, published_date__year=year, published_date__month=month,
                              published_date__day=day, slug=slug)
    return render(request, 'blog/post_detail.html', {
        'post': post
    })

def journal_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/journal_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def resume(request):
    return render(request, 'blog/resume.html')

def sitemap(request):
    return render(request, 'blog/sitemap.xml')

# @login_required
# def post_draft_list(request):
#     posts = Post.objects.filter(Q(published_date__isnull=True) | Q(published_date__gt=timezone.now())).order_by('created_date')
#     return render(request, 'blog/post_draft_list.html', {'posts': posts})