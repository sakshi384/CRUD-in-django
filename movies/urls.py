from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('hello/',views.HelloworldApi.as_view(),name="helloworld"),
    path('create/', views.MovieCreateView.as_view(), name='movie_create'),
    path('list/', views.MovieListView.as_view(), name='movie_list'),

]