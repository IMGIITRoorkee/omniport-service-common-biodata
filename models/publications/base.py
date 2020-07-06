import swapper

from django.db import models


class BasePublication(models.Model):
    """
    This model stores information about a publication
    """

    title = models.CharField(
        max_length=255,
    )

    authors = models.CharField(
        max_length=255,
    )

    publisher = models.CharField(
        max_length=127,
    )

    year = models.IntegerField()

    pages = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    volumes = models.CharField(
        max_length=31,
        blank=True,
    )

    class Meta:
        """
        Meta class for BasePublication
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        title = self.title
        year = self.year

        return f'{title} - {year}'
