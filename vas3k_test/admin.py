from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Category, Post, Travel, Notes, Challenge


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label="Текст", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CatedoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "id")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image", "tittle", "subtittle", "url", "test", "id", "category", "draft")
    readonly_fields = ("get_image",)
    list_display_links = ("id", "name",)
    list_filter = ("category",)
    search_fields = ("tittle", "category__name")
    save_on_top = True
    form = PostAdminForm
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("picture", "get_image"),)
        }),
        (None, {
            "fields": (("name", "tittle", "subtittle"),)
        }),
        (None, {
            "fields": ("text",)
        }),
        ("Options", {
            "classes": ("collapse",),
            "fields": (("url", "category", "test", "draft", "date"),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image", "tittle", "subtittle", "url", "test", "id", "category", "draft")
    readonly_fields = ("get_image",)
    list_display_links = ("id", "name",)
    list_filter = ("category",)
    search_fields = ("tittle", "category__name")
    save_on_top = True
    form = PostAdminForm
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("picture", "get_image"),)
        }),
        (None, {
            "fields": (("name", "tittle", "subtittle"),)
        }),
        (None, {
            "fields": ("text",)
        }),
        ("Options", {
            "classes": ("collapse",),
            "fields": (("url", "category", "test", "draft", "date"),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Notes)
class TravelAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image", "tittle", "subtittle", "url", "test", "id", "category", "draft")
    readonly_fields = ("get_image",)
    list_display_links = ("id", "name",)
    list_filter = ("category",)
    search_fields = ("tittle", "category__name")
    save_on_top = True
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("picture", "get_image"),)
        }),
        (None, {
            "fields": (("name", "tittle", "subtittle"),)
        }),
        (None, {
            "fields": ("text",)
        }),
        ("Options", {
            "classes": ("collapse",),
            "fields": (("url", "category", "test", "draft", "date"),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Challenge)
class TravelAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image", "tittle", "subtittle", "url", "test", "id", "category", "draft")
    readonly_fields = ("get_image",)
    list_display_links = ("id", "name",)
    list_filter = ("category",)
    search_fields = ("tittle", "category__name")
    save_on_top = True
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("picture", "get_image"),)
        }),
        (None, {
            "fields": (("name", "tittle", "subtittle"),)
        }),
        (None, {
            "fields": ("text",)
        }),
        ("Options", {
            "classes": ("collapse",),
            "fields": (("url", "category", "test", "draft", "date"),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.site_title = "Vas3k"
admin.site.site_header = "Vas3k"


