import factory
from factory import DjangoModelFactory, Faker
from blogs.models import Blog, User, Comment


class UserFactory(DjangoModelFactory):
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")

    class Meta:
        model = User

class BlogFactory(DjangoModelFactory):
    title = factory.Iterator(["django capabilities", "graphql capabilities"])
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Blog

class CommentFactory(DjangoModelFactory):
    blog = factory.SubFactory(BlogFactory)
    name = Faker("name")

    class Meta:
        model = Comment
