from django.db import models

from common_biodata.models.publications import BasePublication
from formula_one.utils.upload_to import UploadTo


class AbstractPaper(BasePublication):
    """
    This model stores information about a paper
    """

    journal = models.CharField(
        max_length=255,
    )

    # Override this field in every child class!
    paper = models.FileField(
        upload_to=UploadTo('common_biodata', 'papers'),
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for AbstractPaper
        """

        abstract = True
