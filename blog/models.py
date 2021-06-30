
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

#  create catagory function | catagories

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("blog:blog_by_category", args={self.slug})

# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(Category, blank= True, null= True, on_delete=models.CASCADE,related_name= 'posts')
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='public/')
    tags = TaggableManager()
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    # get.absolute function add
    
    def get_absolute_url(self):
        return reverse("blog:blog_details", kwargs={
            "slug": self.slug })

    # count query function create

    @property
    def comment_count(self):
        return Comment.objects.filter(approve_comment=True).count()

# comment models add

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name= 'comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    approve_comment = models.BooleanField(default=False)


    def __str__(self):
        return self.name





