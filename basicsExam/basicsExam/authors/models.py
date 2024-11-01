from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(
                limit_value=4,
                message='Your name must contain minimum 4 letters'
            ),
            RegexValidator(
                regex='^[A-Za-z]+$',
                message="Your name must contain letters only!"
            ),
        ],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(
                limit_value=2,
                message='Your name must contain minimum 4 letters'
            ),
            RegexValidator(
                regex='^[A-Za-z]+$',
                message="Your name must contain letters only!"
            ),
        ],
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex=r'^\d{6}$',
                message="Your passcode must be exactly 6 digits!"
            )
        ],
        help_text="Your passcode must be a combination of 6 digits.",
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
