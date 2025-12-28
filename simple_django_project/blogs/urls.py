from django.urls import path
from .views import Home, BlogListAPIView, BlogCreateAPIView

app_name = "blogs"
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("api/blogs/", BlogListAPIView.as_view(), name="api_GET_endpoint"),
    path("api/blogs/create/", BlogCreateAPIView.as_view(), name="api_POST_endpoint")
]