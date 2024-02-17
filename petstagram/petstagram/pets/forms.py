from django import forms

from petstagram.pets.models import Pet
class ReadOnlyFieldsFormMixin:
    readonly_fields =()
    def _apply_readonly_fields(self):
        for name,field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


    @property
    def read_only_fields_names(self):
        if self.readonly_fields == '__all__':
            return self.readonly_fields
        return self.readonly_fields

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


class PetEditForm(ReadOnlyFieldsFormMixin,PetBaseForm):
    readonly_fields = ('date_of_birth',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_fields()
    def clean_date_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth != self.instance.date_of_birth:
            raise forms.ValidationError('You can not change date of birth')
        return date_of_birth




class PetDeleteForm(ReadOnlyFieldsFormMixin,PetBaseForm):
    readonly_fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance