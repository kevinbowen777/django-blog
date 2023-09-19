import pytest
from django.test import Client, RequestFactory

from accounts.tests.factories import UserFactory
from posts.models import Post
from posts.tests.factories import CommentFactory, PostFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def post():
    return PostFactory()


@pytest.fixture
def comment():
    return CommentFactory()


@pytest.fixture
def client():
    return Client()


# Create posts for pagination tests
@pytest.fixture
def ten_posts(user):
    posts = []
    for post_id in range(10):
        post_id += 1
        Post.objects.create(
            title="A Tiny Test Blog Post {0}".format(post_id),
            tags="dummy, test, django, blog",
            # slug="2023/9/18/a-tiny-test-blog-post-{0}/".format(post_id),
            body="Some blog post content {0}".format(post_id),
            author=user,
        )
        posts.append(post)
    return posts
