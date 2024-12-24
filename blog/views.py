from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.


def index_view(request):
    return render(request, "index.html")


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Saeed"
        context["posts"] = Post.objects.all()
        return context


class PostList(ListView):

    # queryset = Post.objects.all()
    # model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = ["-id"]

    def get_queryset(self):

        posts = Post.objects.all()
        return posts


class PostDetail(LoginRequiredMixin, DetailView):

    model = Post
