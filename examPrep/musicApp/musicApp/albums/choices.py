from django.db import models


class GenreChoices(models.TextChoices):
    POP = 'POP', 'Pop Music'
    JAZZ = 'JAZZ', 'Jazz Music'
    RB = 'RB', 'R&B Music'
    ROCK = 'ROCK', 'Rock Music'
    COUNTRY = 'COUNTRY', 'Country Music'
    DANCE = 'DANCE', 'Dance Music'
    HIP_HOP = 'HIP_HOP', 'Hip Hop Music'
    OTHER = 'OTHER', 'Other'
