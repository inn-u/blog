from django.urls import path
from .views import HomePageView, SingePostView

urlpatterns = [
    path('', HomePageView.as_view() , name='home'),
    path("<slug:slug>/", SingePostView.as_view(), name="post_detail"),
]
