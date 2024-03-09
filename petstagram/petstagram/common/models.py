from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import PetPhoto

UserModel = get_user_model()

# Create your models here.
class PhotoComments(models.Model):
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
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

class PhotoLikes(models.Model):
        pet_photo = models.ForeignKey(
            PetPhoto,
            on_delete=models.DO_NOTHING,
            related_name='likes'
        )

        user = models.ForeignKey(
            UserModel,
            on_delete=models.RESTRICT,
        )