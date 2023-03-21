from django import template
from rango.models import Movie

register = template.Library()

@register.inclusion_tag('rango/movie.html')
def get_category_list(current_category=None):
    return {'movies': Movie.objects.all(), 'current_movie': current_category}