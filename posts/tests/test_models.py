from datetime import datetime as dt

import pytest

pytestmark = pytest.mark.django_db


def test_post___str__(post):
    assert str(post) == post.title


def test_post_get_absolute_url(post):
    slug_time = dt.now().strftime("%Y/%-m/%-d")
    assert post.get_absolute_url() == f"/posts/{slug_time}/{post.slug}/"


def test_comment__str__(comment):
    assert str(comment) == f"Comment by {comment.name} on {comment.post}"
