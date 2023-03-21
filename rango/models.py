from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

slug = models.SlugField(unique=True)

class Movie(models.Model):
    title = models.CharField(max_length=128, unique=True)
    releaseDate = models.CharField(max_length=128)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name_plural = 'Movies'
    
    def __str__(self):
        return self.title
        
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2)
    user = models.CharField(max_length=128, default="Anonymous User")
    
    def __str__(self):
        return self.rating

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username