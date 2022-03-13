import graphene
from graphene_django import DjangoObjectType
from blogs.models import User, Blog, Comment


class BlogType(DjangoObjectType):
    class Meta:
        model = Blog


class UserType(DjangoObjectType):
    class Meta:
        model = User


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment