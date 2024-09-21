# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import bleach
from django.views.generic import TemplateView

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

    def form_valid(self, form):
        # Sanitize the body content
        allowed_tags = ['p', 'ul', 'li', 'strong', 'em', 'a', 'img', 'h1', 'h2', 'h3', 'blockquote']
        allowed_attrs = {'a': ['href', 'title'], 'img': ['src', 'alt']}
        form.instance.body = bleach.clean(form.instance.body, tags=allowed_tags, attributes=allowed_attrs)
        return super().form_valid(form)

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        # Sanitize the body content
        allowed_tags = ['p', 'ul', 'li', 'strong', 'em', 'a', 'img', 'h1', 'h2', 'h3', 'blockquote']
        allowed_attrs = {'a': ['href', 'title'], 'img': ['src', 'alt']}
        form.instance.body = bleach.clean(form.instance.body, tags=allowed_tags, attributes=allowed_attrs)
        return super().form_valid(form)
    
class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

class AboutView(TemplateView):
    template_name = 'about.html'