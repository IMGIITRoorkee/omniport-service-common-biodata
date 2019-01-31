from django.db import models

from kernel.models.root import Model


class AbstractProfile(Model):
    """
    This model contains information about the home page profile
    """

    handle = models.SlugField(
        max_length=31,
        blank=True,
        unique=True,
    )

    description = models.TextField()

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
