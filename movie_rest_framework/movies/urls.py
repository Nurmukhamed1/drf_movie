from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MovieListView

router = DefaultRouter()
# router.register("viewset", MovieViewSet, basename="moview_viewset")
# router.register("view", MovieListView, basename="moview_view")

urlpatterns = [
    path("movie/", MovieListView.as_view(), name="movie_list"),
]
