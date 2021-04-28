from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import *

# Create your views here.
class HelloworldApi(APIView):
    def get(self,request,format=None):
        return Response(data={"message":"hello world"},status=200)


class MovieCreateView(CreateAPIView):
    serializer_class = MovieSerializer


class MovieListView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer