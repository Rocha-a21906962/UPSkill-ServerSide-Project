from django.contrib import admin
from .models import Genre, Movie

# Register your models here.

admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'year')}
    fields = ('title', 'slug', 'year', 'genres', 'image', 'actors', 'directors')
