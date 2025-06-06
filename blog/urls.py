from django.urls import path

from .views import AboutPage, ListPostView, SingePostView

urlpatterns = [
    path('about/', AboutPage.as_view(), name='about'),
    path('', ListPostView.as_view(), name='post_list'),
    path('<slug:slug>', SingePostView.as_view(), name='post_detail'),
]
