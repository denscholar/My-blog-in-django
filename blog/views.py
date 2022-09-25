from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/home.html'
    ordering = ['-dateCreated']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name='blog/detail.html'
