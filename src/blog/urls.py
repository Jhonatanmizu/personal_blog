from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("post/<slug:slug>/", views.index, name="post"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("page/<int:pk>/", views.page_detail, name="page_detail"),
    path("", views.index, name="blog"),
]
