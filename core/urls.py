from django.urls import path
from .views import home_view, register_view, login_view, logout_view, cabinet_view, create_order_view

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cabinet/", cabinet_view, name="cabinet"),
    path("order/new/", create_order_view, name="order_new"),
]