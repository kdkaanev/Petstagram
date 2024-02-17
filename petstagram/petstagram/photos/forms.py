from django import forms

from petstagram.photos.models import PetPhoto

class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        exclude = ['photo']