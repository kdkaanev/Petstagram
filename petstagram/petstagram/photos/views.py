from django.shortcuts import render

from petstagram.photos.models import PetPhoto


# Create your views here.
def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')


class Photo:
    pass


def details_photo(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk),
    }
    return render(request, 'photos/photo-details-page.html', context)
