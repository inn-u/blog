from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Post, PostImage, Tag, Category


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    exclude = ('slug',)
    list_display = ('title', 'is_featured', 'published_date')
    list_editable = ('is_featured',)
    list_filter = ('is_featured', 'published_date')
    filter_horizontal = ('tags',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change and Category.objects.count() >= 6:
            raise ValidationError('Only 6 categories allowed.')
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
