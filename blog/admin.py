from django.contrib import admin

from .models import Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    exclude = ('slug',)
    list_display = ('title', 'is_featured', 'published_date')
    list_editable = ('is_featured',)
    list_filter = ('is_featured', 'published_date')


admin.site.register(Post, PostAdmin)
