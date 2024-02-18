from django.shortcuts import render, redirect

from petstagram.photos.models import PetPhoto
from petstagram.common.models import PhotoLikes


# Create your views here.
def index(request):
    pet_name_pattern = request.GET.get('pet_name_pattern', None)
    pets_photos = PetPhoto.objects.all()

    if pet_name_pattern:
        pets_photos = pets_photos.filter(pets__name__icontains=pet_name_pattern)

    context = {
        'pet_photos': pets_photos,
        'pet_name_pattern': pet_name_pattern

    }
    return render(request, 'common/home-page.html', context)

# Create your views here.





def like_pet_photo(request,pk):
    #pet_photo_like = PhotoLikes.objects.get(pk=pk, user=request.user)
    pet_photo_like = PhotoLikes.objects.filter(pet_photo_id=pk).first()
    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLikes.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{pk}')
