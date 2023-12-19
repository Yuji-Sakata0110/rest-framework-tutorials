from django.urls import include, path, URLResolver
from rest_framework import routers
from myapp import views

# 各View関数をデフォルトルーターとしてセットする。
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns: list[URLResolver] = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]

# 各URLパターンにデフォルトルータのURLを追加する。
urlpatterns += router.urls
