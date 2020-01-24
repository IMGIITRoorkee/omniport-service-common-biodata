from django.db import models

from common_biodata.constants import graduations


class AbstractEducation(models.Model):
    """
    This model contains information about one bit of education
    """

    year = models.IntegerField()

    institute = models.CharField(
        max_length=127,
    )

    field = models.CharField(
        max_length=127,
        blank=True,
        help_text='This can be a stream like Science or Commerce for school education',
    )

    degree = models.CharField(
        max_length=127,
        help_text='This can be a class like Class X or Class XII for school education'
    )

    graduation = models.CharField(
        max_length=3,
        choices=graduations.GRADUATIONS,
    )

    class Meta:
        """
        Meta class for AbstractEducation
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        graduation = self.graduation
        degree = self.degree
        institute = self.institute
        year = self.year
        return f'{graduation} ({degree}) from {institute} in {year}'
