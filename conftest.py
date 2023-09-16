import pytest
from django.test import RequestFactory

from accounts.tests.factories import UserFactory
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
