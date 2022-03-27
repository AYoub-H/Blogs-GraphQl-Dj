import pytest
from tests.blogs.factories import BlogFactory, UserFactory, CommentFactory
from blogs.models import Blog, User

@pytest.mark.django_db
def test_user_model():
    user = UserFactory()
    assert user.id
    assert isinstance(user, User)

@pytest.mark.django_db
def test_blog_model():
    post = BlogFactory()
    assert post.id
    assert isinstance(post, Blog) 

@pytest.mark.django_db
def test_comment_model():
    comment = CommentFactory()
    assert comment.id
