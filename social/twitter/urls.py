from django.urls import path
from .views import (
    dashboard, profile, main,
    register_request, login_request,
    logout_request, post_tweet)

app_name = "twitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("homepage/", main, name="homepage"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
    path("post-tweet/", post_tweet, name="post_tweet"),

]
