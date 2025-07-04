from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest
from django_summernote.admin import SummernoteModelAdmin

from .models import Category, Page, Post, Tag


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")
    list_per_page = 10
    ordering = ("-id",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "created_by",
    )
    list_display_links = ("title",)
    search_fields = (
        "id",
        "slug",
        "title",
        "excerpt",
        "content",
    )
    list_per_page = 50
    list_filter = (
        "category",
        "is_published",
    )
    list_editable = ("is_published",)
    ordering = ("-id",)
    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
    autocomplete_fields = (
        "tags",
        "category",
    )
    summernote_fields = ("content",)

    def save_model(
        self, request: HttpRequest, obj: Post, form: Any, change: Any
    ) -> None:
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)
        return super().save_model(request, obj, form, change)
