from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed("pages/home.html")
        # self.assertTemplateUsed(self.response, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "A blog website built with Django")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This text does not belong.")

    def test_hompage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed("pages/about.html")
        # self.assertTemplateUsed(self.response, "pages/about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This text does not belong.")

    def test_aboupage_url_resolves_homepageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
