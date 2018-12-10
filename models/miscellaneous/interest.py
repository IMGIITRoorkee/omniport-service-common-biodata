from django.db import models

from kernel.models.root import Model


class AbstractInterest(Model):
    """
    This model contains the interests of the faculty member
    """

    topic = models.CharField(
        max_length=255,
    )

    class Meta:
        """
        Meta class for AbstractInterest
        """
        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        topic = self.topic
        return f'{topic}'
