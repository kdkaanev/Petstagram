from django.shortcuts import render, redirect

from petstagram.photos.models import PetPhoto
from petstagram.common.models import PhotoLikes


# Create your views here.
def index(request):
    pattern = request.GET.get('pattern', None)
    pets_photo = PetPhoto.objects.all()

    if pattern:
        pets_photo = pets_photo.filter(pets__name__icontains=pattern)
    context = {
        'pet_photos':PetPhoto.objects.all(),
        'pets': pets_photo
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
