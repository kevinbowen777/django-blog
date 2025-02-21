"""Sphinx configuration."""

project = "django-blog"
author = "Kevin Bowen"
copyright = f"2025, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "django-blog"
extensions = [
    "sphinx.ext.duration",
]
