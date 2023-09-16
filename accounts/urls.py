from django.urls import path
from accounts import views
from accounts.views.userdata import userdata

app_name = "accounts"


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
    path("profile-creation/",userdata,name="profile-creation"),
]
