from django.db import models

from petstagram.photos.models import PetPhoto


# Create your models here.
class PhotoComents(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,

    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        auto_now=True
    )

    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING,
        related_name='comments'
    )

    class PhotoLikes(models.Model):
        pet_photo = models.ForeignKey(
            PetPhoto,
            on_delete=models.DO_NOTHING,
            related_name='likes'
        )
