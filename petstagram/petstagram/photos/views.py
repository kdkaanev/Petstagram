from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import PetPhoto


# Create your views here.
def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('details-photo')
    context = {
        'form': form,
    }
    return render(request, 'photos/photo-add-page.html',context=context)


def edit_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    form = PhotoCreateForm(request.POST or None)
    context = {
        'form': form,
        'pet_photo': pet_photo,
    }

    if request.method == 'POST':
        form = PhotoCreateForm(request.POST, instance=pet_photo)
        if form.is_valid():
            form.save()
            return redirect('details-photo', pk=pet_photo.pk)
    return render(request, 'photos/photo-edit-page.html', context)


class Photo:
    pass


def details_photo(request, pk):
    context = {
        'pet_photo': PetPhoto.objects.get(pk=pk),
    }
    return render(request, 'photos/photo-details-page.html', context)
