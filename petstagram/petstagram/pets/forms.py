from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo', ]

        widgets = {
           'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            'name': 'Pet name',
            'personal_photo': 'Link to image',
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['readonly'] = True
    def clean_date_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth != self.instance.date_of_birth:
            raise forms.ValidationError('You can not change date of birth')
        return date_of_birth