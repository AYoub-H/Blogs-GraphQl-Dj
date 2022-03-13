import graphene
from blogs.graphql.types import UserType, BlogType
from blogs.models import Blog, User


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Meta:
        description = "Add user details"

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        user = User.objects.create(last_name=kwargs.get('last_name'),
                                   email=kwargs.get('email'))
        return CreateUserMutation(user=user)


class CreateBlogMutation(graphene.Mutation):
    blog = graphene.Field(BlogType)

    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        blog = Blog.objects.create(title=kwargs.get('title'),
                                   author=kwargs.get('author'))
        return CreateBlogMutation(blog=blog)
