from datetime import datetime as dt

import factory
import factory.fuzzy
from django.template.defaultfilters import slugify

from accounts.tests.factories import UserFactory

from ..models import Comment, Post


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="Breaking News: ")
    body = factory.fuzzy.FuzzyText(length=50)
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    # slug = slugify(title)
    publish = dt.now()
    # publish = factory.fuzzy.FuzzyDate(datetime.date(2022, 6, 23))
    status = "PB"
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Post


class CommentFactory(factory.django.DjangoModelFactory):
    post = factory.SubFactory(PostFactory)
    name = factory.SubFactory(UserFactory)
    email = "test_dummy@example.com"
    # email = f"{name.username}@example.com"
    body = factory.fuzzy.FuzzyText(length=50)

    class Meta:
        model = Comment
