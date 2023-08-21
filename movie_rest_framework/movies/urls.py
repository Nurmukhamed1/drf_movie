from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MovieListView, MovieDetailView

router = DefaultRouter()

urlpatterns = [
    path("movie/", MovieListView.as_view(), name="movie_list"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
]
