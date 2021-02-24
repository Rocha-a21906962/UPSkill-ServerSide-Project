from django.contrib import admin
from .models import Genre, Movie

# Register your models here.

admin.site.register(Genre)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # TODO: Como concatenar e o que por!
    prepopulated_fields = {'slug': ('title',)}
