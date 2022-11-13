from django.urls import path

from .views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView,
)

urlpatterns = [
    path(
        "posts/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"
    ),
    path("posts/new/", BlogCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("posts/", BlogListView.as_view(), name="post_list"),
]
