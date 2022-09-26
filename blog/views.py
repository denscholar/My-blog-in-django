from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


# Read Posts/Display all post
class BlogListView(ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'posts'
    template_name='blog/home.html'
    ordering = ['-dateCreated']


# Display content/detail of post
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name='blog/detail.html'

# Create Post
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    fields = ['title', 'body']
    template_name = "blog/create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update Post
class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    fields = ['title', 'body']
    template_name = "blog/create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Delete Post
class PostDeleteView(SuccessMessageMixin, DeleteView):
    success_url = '/'
    model = Post
    template_name = "blog/delete.html"
    success_message = "Post was sucessfully deleted"
