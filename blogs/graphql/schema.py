import graphene
# from graphene import relay

from blogs.graphql.types import UserType, BlogType, CommentType
from blogs.models import Blog, User, Comment


class BlogQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    # user = graphene.Field(
    #     UserType,
    #     id=graphene.ID(required=False),
    # )
    blogs = graphene.List(BlogType)
    comments = graphene.List(CommentType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_blogs(self, info):
        return Blog.objects.all()

    def resolve_comments(self, info):
        return Comment.objects.all()

    # def resolve_user(self, info, **kwargs):
    #     user_id = kwargs.get("id")
    #     if user_id:
    #         return
    #     return None


schema = graphene.Schema(query=BlogQuery)
