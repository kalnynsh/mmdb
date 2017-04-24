from django.db import models


class MovieDetails(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stars = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    movie = models.ForeignKey(MovieDetails, related_name='reviews')
    user_name = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.movie
