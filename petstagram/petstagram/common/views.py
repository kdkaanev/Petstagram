from django.shortcuts import render, redirect

from petstagram.photos.models import PetPhoto
from petstagram.common.models import PhotoLikes


# Create your views here.
def index(request):
    context = {
        'pet_photos':PetPhoto.objects.all()
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
