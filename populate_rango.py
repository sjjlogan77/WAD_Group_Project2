import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD_group_project.settings')

import django
django.setup()
from rango.models import Movie, Rating

def populate():
    
    harry_potter_ratings = [ {"user1":5},{"user2":6},{"user3":8},{"user4":9},{"user5":3} ]

    cars_ratings = [ {"user1":6},{"user2":4},{"user3":7},{"user4":9},{"user5":7} ]
    
    home_alone_ratings = [ {"user1":5},{"user2":1},{"user3":6},{"user4":9},{"user5":3} ]
    
    movies = {'Harry Potter': harry_potter_ratings,'Cars': cars_ratings, 'Home Alone': home_alone_ratings}
    
    for movie, movie_data in movies.items():
        if (movie=='Harry Potter'):
            c = add_movie(movie, '1982-01-20')
        elif (movie=='Cars'):
            c = add_movie(movie, '1972-02-30')
        elif (movie=='Home Alone'):
            c = add_movie(movie, '1986-03-10')
        for user, rating in movie_data.items():
            add_rating(c, movie, user, rating)
          
    for c in Movie.objects.all():
        for p in Rating.objects.filter(movie=c):
            print(f'- {c}: {p}')
            
def add_rating(movie, title, rating, user):
    p = Rating.objects.get_or_create(movie=movie, title=title)[0]
    p.rating=rating
    p.user=user
    p.save()
    return p
    
def add_movie(title, releaseDate):
    c = Movie.objects.get_or_create(title=title)[0]
    c.releaseDate=releaseDate
    c.save()
    return c
    
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()