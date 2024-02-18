from django.contrib import admin

from petstagram.common.models import PhotoComments


# Register your models here.
@admin.register(PhotoComments)
class PhotoCommentsAdmin(admin.ModelAdmin):
    pass
