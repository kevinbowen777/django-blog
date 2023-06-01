from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    comment_add,
    post_detail,
    post_list,
    post_share,
)

urlpatterns = [
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/new/", PostCreateView.as_view(), name="post_new"),
    path(
        "posts/<int:year>/<int:month>/<int:day>/<slug:post>/",
        post_detail,
        name="post_detail",
    ),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/", post_list, name="post_list"),
    path("posts/<int:post_id>/share/", post_share, name="post_share"),
    path("posts/<int:post_id>/comment/", comment_add, name="comment_add"),
]
