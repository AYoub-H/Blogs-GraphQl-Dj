from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    """User Model """
    first_name = models.CharField(_("First name"), max_length=40, blank=True, null=True)
    last_name = models.CharField(_("Last name"), max_length=40, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(
        _("Date joined"), auto_now_add=True, editable=False
    )
    phone_number = PhoneNumberField(_("Phone"), blank=True, null=True, )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True, editable=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Blog(models.Model):
    """Represent blog Model"""

    class BlogStatus(models.TextChoices):
        DRAFT = "DRAFT", _("Draft")
        PUBLISHED = "PUBLISHED", _("Published")

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    content = models.TextField()
    status = models.CharField(max_length=32, choices=BlogStatus.choices, default=BlogStatus.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Represent users comments Model"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog}'