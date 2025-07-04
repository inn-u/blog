from django.urls import path

from .views import (
    AboutPage,
    ContactPage,
    Error404,
    ListPostView,
    SinglePostView,
    PhotoGallery,
)

urlpatterns = [
    path('about/', AboutPage.as_view(), name='about'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('preview-404/', Error404.as_view(), name='preview-404/'),
    path('', ListPostView.as_view(), name='post_list'),
    path('gallery/', PhotoGallery.as_view(), name='gallery'),
    path('<slug:slug>/', SinglePostView.as_view(), name='post_detail'),
    path('tag/<slug:tag_slug>/', ListPostView.as_view(), name='posts_by_tag'),
    path(
        'category/<slug:category_slug>/', ListPostView.as_view(), name='post_category'
    ),
]
