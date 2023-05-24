from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class BlogListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "posts/post_list.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class BlogCreateView(CreateView):
    model = Post
    template_name = "posts/post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("home")
