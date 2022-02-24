from django.urls import path
from .view import BlogListView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]
