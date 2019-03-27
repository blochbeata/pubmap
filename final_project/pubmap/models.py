from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models



# Create your models here.
RATING = (
    (1, "spokojnie usiądziesz"),
    (2, "pośpiesz się"),
    (3, "jak masz szczęście, to coś znajdziesz"),
    (4, "postoisz"),
    (5, "nawet nie wejdziesz")
)


class Pub(models.Model):
    name = models.CharField(max_length=255)
    formatted_address = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255, unique=True)
    formatted_phone_number = models.CharField(max_length=16, null=True)
    website = models.URLField(null=True)
    opening_hours = JSONField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    rating = models.IntegerField(choices=RATING)
    posted = models.DateTimeField(auto_now_add=True)
    pub = models.ForeignKey(Pub, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)


