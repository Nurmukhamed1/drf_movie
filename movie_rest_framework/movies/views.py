from rest_framework import views
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


class MovieListView(views.APIView):
    def get(self, request):
        queryset = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(queryset, many=True)
        return Response(serializer.data)


class MovieDetailView(views.APIView):
    def get(self, request, pk):
        queryset = Movie.objects.filter(id=pk, draft=False)
        serializer = MovieDetailSerializer(queryset)
        return Response(serializer.data)
