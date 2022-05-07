from django.contrib import admin

from blogs.models import User, Blog, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    model = Blog

    list_display = (
        "id",
        "title",
        "status",
        "slug",
        "created_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
