from django.shortcuts import render, get_object_or_404

# Create your views here.
from movie.models import Movie

def movie_list(request):
    """ """
    movies = Movie.objects.all()

    return render(request,
                  'movie/list.html',
                  {'movies': movies})


def movie_detail(request, id):
    """ """
    movie = get_object_or_404(Movie, id=id)

    return render(request, 'movie/detail.html',
                  {'movie': movie})


def movie_search(request):
    search_string = request.GET.get("query")
    if search_string:
        results = Movie.objects.filter(title__contains=search_string)
    else:
        results = None

    return render(request,
                  'movie/search.html',
                  {'results': results})
