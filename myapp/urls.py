from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns: list = [
    path("", include(router.urls)),
]
