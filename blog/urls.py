# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView # type: ignore

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), # new # type: ignore
    path("", BlogListView.as_view(), name="home"),
]