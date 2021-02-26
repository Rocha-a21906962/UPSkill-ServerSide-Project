from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:id>/', views.movie_detail, name='movie_detail'),
    path('search', views.movie_search, name='movie_search')
]
