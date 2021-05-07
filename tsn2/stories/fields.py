from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class XField(models.FloatField):
    default_validators = [
        MinValueValidator(-90),
        MaxValueValidator(90),
    ]


class YField(models.FloatField):
    default_validators = [
        MinValueValidator(-180),
        MaxValueValidator(180),
    ]
