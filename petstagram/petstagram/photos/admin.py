from django.contrib import admin


from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)

class PhotoAdmin(admin.ModelAdmin):
    pass