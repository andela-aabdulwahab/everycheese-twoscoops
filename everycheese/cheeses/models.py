from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField


class Cheese(models.Model):

    FIRMNESS_UNSPECIFIED = 'unspecified'
    FIRMNESS_SOFT = 'soft'
    FIRMNESS_SEMI_SOFT = 'semi-soft'
    FIRMNESS_SEMI_HARD = 'semi-hard'
    FIRMNESS_HARD = 'hard'

    FIRMNESS_CHOICES = (
        (FIRMNESS_UNSPECIFIED, 'Unspecified'),
        (FIRMNESS_SOFT, 'Soft'),
        (FIRMNESS_SEMI_SOFT, 'Semi-Soft'),
        (FIRMNESS_SEMI_HARD, 'Semi-Hard'),
        (FIRMNESS_HARD, 'Hard'),
    )

    name = models.CharField("Name of cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False,
                         populate_from='name')
    description = models.TextField("Description of Cheese", blank=True)
    firmness = models.CharField("Firmness", choices=FIRMNESS_CHOICES,
                                default=FIRMNESS_UNSPECIFIED, max_length=20)
    country_of_origin = CountryField('Country of Origin', blank=True)

    def __str__(self):
        return self.name
