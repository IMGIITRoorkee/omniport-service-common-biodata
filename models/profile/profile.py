from django.db import models

from formula_one.models.base import Model
from common_biodata.utils.updated_URLValidator import UpdatedURLValidator


class AbstractProfile(Model):
    """
    This model contains information about the home page profile
    """

    handle = models.SlugField(
        max_length=31,
        blank=True,
        null=True,
        default=None,
        unique=True,
    )

    description = models.TextField()

    personal_website = models.CharField(
        max_length=255,
        blank=True,
        validators=[UpdatedURLValidator()],
    )

    class Meta:
        """
        Meta class for AbstractProfile
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        handle = self.handle
        return f'handle : {handle}'
