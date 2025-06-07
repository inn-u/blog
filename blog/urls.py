from django.urls import path

from .views import AboutPage, ContactPage, Error404, ListPostView, SingePostView

urlpatterns = [
    path('about/', AboutPage.as_view(), name='about'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('preview-404/', Error404.as_view(), name='preview-404/'),
    path('', ListPostView.as_view(), name='post_list'),
    path('<slug:slug>/', SingePostView.as_view(), name='post_detail'),
]
