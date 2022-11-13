from accounts.tests.factories import UserFactory

from django.test import TestCase

from .factories import PostFactory

# from ..models import Review


class PostTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.post = PostFactory()
        """
        self.review = Review.objects.create(
            post=self.post,
            creator=self.user,
            review="An excellent review",
        )
        """

    def test__str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title

    def test_get_absolute_url(self):
        url = self.post.get_absolute_url()
        assert url == f"/posts/{self.post.id}/"


"""
    def test_review__str__(self):
        assert self.review.__str__() == self.review.review
        assert str(self.review) == self.review.review

    def test_review_get_absolute_url(self):
        url = self.review.get_absolute_url()
        assert url == f'{"/posts/"}'


from django.test import TestCase


class PostTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.post = PostFactory()
        self.review = Review.objects.create(
            post=self.post,
            creator=self.user,
            review="An excellent review",
        )

    def test__str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title

    def test_get_absolute_url(self):
        url = self.post.get_absolute_url()
        assert url == f"/posts/{self.post.id}/"


    def test_review__str__(self):
        assert self.review.__str__() == self.review.review
        assert str(self.review) == self.review.review

    def test_review_get_absolute_url(self):
        url = self.review.get_absolute_url()
        assert url == f'{"/posts/"}'
"""
