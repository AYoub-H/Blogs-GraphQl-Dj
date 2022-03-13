from factory import DjangoModelFactory, Faker
from blogs.models import Blog, User, Comment


class UserFactory(DjangoModelFactory):
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")

    class Meta:
        model = User

