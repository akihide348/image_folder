from django.urls import path

from .views import HomePageView, CreatePostView#,DeletePostView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('post/', CreatePostView.as_view(), name='add_post'),
    #path('', DeletePostView.as_view(), name='delete_post'),
]
