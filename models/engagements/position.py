from django.db import models

from formula_one.mixins.period_mixin import BlurryPeriodMixin


class AbstractPosition(BlurryPeriodMixin, models.Model):
    """
    This model contains information about a position
    """

    position = models.CharField(
        max_length=127,
    )

    organisation = models.CharField(
        max_length=127,
    )

    description = models.TextField()

    class Meta:
        """
        Meta class for AbstractPosition
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        position = self.position
        organisation = self.organisation
        return f'{position} at {organisation}'
