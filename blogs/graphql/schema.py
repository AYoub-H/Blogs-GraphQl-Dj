import graphene
from blogs.graphql.types import UserType, BlogType, CommentType
from blogs.models import Blog, User, Comment


class BlogQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    blogs = graphene.List(BlogType)
    comments = graphene.List(CommentType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_blogs(self, info):
        return Blog.objects.all()

    def resolve_comments(self, info):
        return Comment.objects.all()


schema = graphene.Schema(query=BlogQuery)