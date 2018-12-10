from django.db import models

from common_biodata.models.publications import BasePublication


class AbstractBook(BasePublication):
    """
    This model stores information about a book
    """

    contribution = models.CharField(
        max_length=255,
        blank=True,
    )

    editors = models.CharField(
        max_length=255,
        blank=True,
    )

    isbn_code = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='ISBN code',
    )

    class Meta:
        """
        Meta class for AbstractBook
        """

        abstract = True
