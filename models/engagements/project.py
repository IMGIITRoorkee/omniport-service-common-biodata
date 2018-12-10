from django.db import models

from kernel.mixins.period_mixin import BlurryPeriodMixin
from kernel.utils.upload_to import UploadTo


class AbstractProject(BlurryPeriodMixin, models.Model):
    """
    This class contains information about a project
    """

    topic = models.CharField(
        max_length=127,
    )

    field = models.CharField(
        max_length=127,
    )

    # Override this field in every child class!
    image = models.ImageField(
        upload_to=UploadTo('common_biodata', 'projects'),
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        """
        Meta class for AbstractProject
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        topic = self.topic
        field = self.field
        return f'{topic}, {field}'
