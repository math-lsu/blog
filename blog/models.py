# blog/models.py
from django.db import models
from django.urls import reverse
import bleach

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        allowed_tags = ['p', 'ul', 'li', 'strong', 'em', 'a', 'img', 'h1', 'h2', 'h3', 'blockquote']
        allowed_attrs = {'a': ['href', 'title'], 'img': ['src', 'alt']}
        self.body = bleach.clean(self.body, tags=allowed_tags, attributes=allowed_attrs)
        super().save(*args, **kwargs)