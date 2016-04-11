from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    likes= models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
             self.slug = slugify(self.name)
             super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class Page(models.Model):

    category=models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url=models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
'''
class Userprofile(models.Model):

    # this line is requred because it links userprofile to User model instance .
    user = models.OneToOneField(User)
    
    # the additional attributes that we wish to include 
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to = 'profile_images', blank = True)
    bio = models.TextField(max_length=500, null = True, blank=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):

    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingback = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

'''