from datetime import datetime as dt

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Comment, Post


class PostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="leopoldbloom",
            email="leopoldbloom@example.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            slug="a-good-title",
            author=self.user,
        )

        self.post2 = Post.objects.create(
            title="A good second title",
            body="Nice body content for a second post",
            # slug="a-good-title",
            author=self.user,
            status="DF",
        )
        self.slug_time = dt.now().strftime("%Y/%-m/%-d")

    def test___str__(self):
        assert self.post.__str__() == self.post.title
        assert str(self.post) == self.post.title

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.slug}", "a-good-title")
        self.assertEqual(f"{self.post2.slug}", "a-good-second-title")
        self.assertEqual(f"{self.post.author}", "leopoldbloom")
        self.assertEqual(f"{self.post.body}", "Nice body content")
        self.assertEqual(f"{self.post.status}", "PB")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(), f"/posts/{self.slug_time}/{self.post.slug}/"
        )

    def test_post_detail_view(self):
        self.client.login(email="johndoe@example.com", password="secret")
        response = self.client.get(f"/posts/{self.slug_time}/{self.post.slug}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "posts/post_detail.html")

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
        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):
        self.client.login(email="leopolbloom@example.com", password="secret")
        response = self.client.get(reverse("post_delete", args={self.post.id}))
        # response = self.client.get(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)


class PostListViewTest(TestCase):
    def setUp(self):
        url = reverse("post_list")
        self.response = self.client.get(url)

        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            slug="a-good-title",
            author=self.user,
        )

        """
        # Create posts for pagination tests
        number_of_posts = 10
        for post_id in range(number_of_posts):
            Post.objects.create(
                title="A Tiny Test Post {0}".format(post_id),
                slug="2023/7/15/a-tiny-test-post-{0}/".format(post_id),
                body="Some post content {0}".format(post_id),
                author=self.user,
            )
        """

    def test_view_url_exists_at_desired_location(self):
        # response = self.client.get("/posts/")
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "posts/post_list.html")


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
            slug="a-good-title",
            author=self.user,
        )

        self.comment = Comment.objects.create(
            post=self.post,
            name="Ron Swoboda",
            email="ron@amazingmets.org",
            body="This is a comment",
        )

    def test_comment_content(self):
        self.assertEqual(f"{self.comment.name}", "Ron Swoboda")
        self.assertEqual(f"{self.comment.email}", "ron@amazingmets.org")
        self.assertEqual(f"{self.comment.body}", "This is a comment")

    def test_comment_add_view(self):
        self.client.login(email="ron@amazingmets.org", password="secret")
        response = self.client.post(
            reverse("comment_add", args={self.post.id}),
            {
                "name": "Ron Swoboda",
                "email": "ron@amazingmets.org",
                "body": "This is a new comment",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.last().body, "This is a new comment")
        self.assertTrue(self.comment.email == self.comment.email)


class SitemapTests(TestCase):
    def setUp(self):
        # url = reverse("sitemap")
        url = "/sitemap.xml"
        self.response = self.client.get(url)

    def test_view_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)


class RSSFeedTests(TestCase):
    def setUp(self):
        url = reverse("post_feed")
        self.response = self.client.get(url)

    def test_feed_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)
