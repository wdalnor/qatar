from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable= False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True , default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name="posts",default=1)
    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
    
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)


