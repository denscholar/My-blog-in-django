from django.urls import path
from .views import BlogListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView 

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete")
]
