from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # noqa:F401

from ..models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="leopoldbloom",
            email="leopoldbloom@example.com",
            password="secret",
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            slug="a-good-title",
            author=cls.user,
        )

    def test___str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.slug}", "a-good-title")
        self.assertEqual(f"{self.post.author}", "leopoldbloom")
        self.assertEqual(f"{self.post.body}", "Nice body content")

    """
    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(), "/posts/{self.post.id}/")
        # self.assertEqual(self.post.get_absolute_url(), "/posts/1/")

    def test_post_detail_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get("/posts/{self.post.id}/")
        # no_response = self.client.get("posts/100000/")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "posts/post_detail.html")
    """

    def test_post_create_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "A good title")
        self.assertEqual(Post.objects.last().body, "Nice body content")

    def test_post_update_view(self):
        self.client.login(email="leopoldbloom@example.com", password="secret")
        response = self.client.get(
            reverse("post_edit", args={self.post.id}),
            # reverse("post_edit", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        self.client.login(email="leopolbloom@example.com", password="secret")
        response = self.client.get(reverse("post_delete", args={self.post.id}))
        # response = self.client.get(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)


"""
class CommentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=self.user,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            comment="A good comment",
            author=self.user,
        )

    def test___str__(self):
        assert self.comment.__str__() == self.comment.comment
        assert str(self.comment) == self.comment.comment

    def test_get_absolute_url(self):
        self.assertEqual(self.comment.get_absolute_url(), "/posts/")
"""
