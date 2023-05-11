import pytest
from django.urls import resolve, reverse

from .factories import PostFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def post():
    return PostFactory()


def test_post_list_reverse():
    """post_list should reverse to /posts/."""
    assert reverse("post_list") == "/posts/"


def test_post_list_resolve():
    """/posts/" should resolve to post_list."""
    assert resolve("/posts/").view_name == "post_list"


def test_post_add_reverse():
    """post_new should reverse to /posts/new/."""
    assert reverse("post_new") == "/posts/new/"


def test_post_add_resolve():
    """/posts/new/" should resolve to post_new."""
    assert resolve("/posts/new/").view_name == "post_new"


def test_post_detail_reverse(post):
    """post_detail should reverse to /posts/uuid."""
    url = reverse("post_detail", kwargs={"pk": post.id})
    assert url == f"/posts/{post.id}/"


def test_post_detail_resolve(post):
    """/posts/{post.id}/ should resolve to post_detail."""
    url = f"/posts/{post.id}/"
    assert resolve(url).view_name == "post_detail"
