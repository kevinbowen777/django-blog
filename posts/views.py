from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class BlogListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "posts/post_list.html"


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/post_new.html"
    fields = ["title", "author", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
