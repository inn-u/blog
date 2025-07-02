from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from config.utils.slugify_utils import slugify, slug_trim, SlugUnique


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=70, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slug_trim(slugify(self.name), max_length=70)
            self.slug = SlugUnique(self.__class__, max_length=70)(base_slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='posts', null=True
    )
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slug_trim(slugify(self.title))
            slug_unique = SlugUnique(model_cls=self.__class__)
            self.slug = slug_unique(base_slug)

        if self.is_featured:
            Post.objects.filter(is_featured=True).update(is_featured=False)

        super().save(*args, **kwargs)

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
    )


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def post_count(self):
        return self.posts.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            max_len = self._meta.get_field('slug').max_length
            base_slug = slug_trim(slugify(self.name), max_length=max_len)
            self.slug = SlugUnique(self.__class__, max_length=max_len)(base_slug)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-creation_date']

    def is_reply(self):
        return self.parent is not None

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'
