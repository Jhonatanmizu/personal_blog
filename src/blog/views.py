from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'blog/pages/index.html')


def post_detail(request: HttpRequest):
    return render(request, 'blog/pages/post.html')


def page_detail(request: HttpRequest):
    return render(request, 'blog/pages/page.html')
