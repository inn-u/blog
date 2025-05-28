from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="post_images/", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
