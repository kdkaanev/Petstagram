from django.contrib import admin


from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'photo', 'description', 'location', 'tagged_pets_count', 'short_description',)


    def tagged_pets_count(self, obj):
        return ', '.join([pet.name for pet in obj.pets.all()])

    def short_description(self, obj):
        return obj.description[:5]