from django import forms

from petstagram.pets.forms import ReadOnlyFieldsFormMixin
from petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ['photo', 'description', 'location', 'pets']


class PhotoCreateForm(PetPhotoBaseForm):
    pass


class PhotoEditForm(ReadOnlyFieldsFormMixin, PetPhotoBaseForm):
    readonly_fields = ('photo',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_fields()






