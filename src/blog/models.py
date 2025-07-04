from django.contrib.auth.models import User
from django.db import models

from app.utils.images import resize_image
from app.utils.rand import slugify_new


class Tag(models.Model):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, default=None, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify_new(self.name)}"
        return super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=None, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify_new(self.name)}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Page(models.Model):
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=65)
    slug = models.SlugField(max_length=255, default=None, blank=True, unique=True)
    is_published = models.BooleanField(default=False)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify_new(self.title)}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by("-pk")


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    objects = PostManager()

    title = models.CharField(
        max_length=65,
    )
    slug = models.SlugField(
        unique=True, default="", null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
    )
    content = models.TextField()
    cover = models.ImageField(upload_to="posts/%Y/%m/", blank=True, default="")
    cover_in_post_content = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # user.post_created_by.all
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_created_by",
    )
    updated_at = models.DateTimeField(auto_now=True)
    # user.post_updated_by.all
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="post_updated_by",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    tags = models.ManyToManyField(Tag, blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)

        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save
