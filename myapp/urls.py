from django.urls import include, path, URLResolver
from rest_framework import routers

from . import views

# 各View関数をデフォルトルーターとしてセットする。
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns: list[URLResolver] = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

# 各URLパターンにデフォルトルータのURLを追加する。
urlpatterns += router.urls
