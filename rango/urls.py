from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('movie/<slug:movie_name_slug>/', views.show_movie, name='show_movie'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<slug:movie_name_slug>/add_rating/', views.add_rating, name='add_rating'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('HOMEPAGE/',views.HOMEPAGE, name='HOMEPAGE'),
]