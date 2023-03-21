from django.contrib import admin
from rango.models import Movie, Rating, UserProfile

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'movie')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(UserProfile)

