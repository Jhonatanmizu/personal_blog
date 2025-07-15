from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from blog.models import Post

POST_PER_PAGE = 9


def filter_posts():
    return Post.objects.filter(is_published=True).order_by("-pk")


def index(request: HttpRequest):
    posts = filter_posts()
    paginator = Paginator(posts, POST_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get("page", 1))
    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def post_detail(request: HttpRequest):
    return render(request, "blog/pages/post.html")


def page_detail(request: HttpRequest):
    return render(request, "blog/pages/page.html")
