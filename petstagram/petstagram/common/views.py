from django.shortcuts import render, redirect
from django.views.generic import ListView

from petstagram.photos.models import PetPhoto
from petstagram.common.models import PhotoLikes


# Create your views here.
# def index(request):
#     pet_name_pattern = request.GET.get('pet_name_pattern', None)
#     pets_photos = PetPhoto.objects.all()
#
#     if pet_name_pattern:
#         pets_photos = pets_photos.filter(pets__name__icontains=pet_name_pattern)
#
#     context = {
#         'pet_photos': pets_photos,
#         'pet_name_pattern': pet_name_pattern
#
#     }
#     return render(request, 'common/home-page.html', context)

# Create your views here.
class IndexView(ListView):
    queryset = PetPhoto.objects.all().prefetch_related('pets__pet_photos__likes').prefetch_related('comments')
    template_name = 'common/home-page.html'

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_name_pattern'] = self.pet_name_pattern or ''
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_pet_name_patterns(queryset)
        return queryset


    def filter_by_pet_name_patterns(self, queryset):
        pet_name_pattern = self.pet_name_pattern
        filter_query = {}
        if pet_name_pattern:
           filter_query['pets__name__icontains'] = pet_name_pattern
        return queryset.filter(**filter_query)



def like_pet_photo(request,pk):
    #pet_photo_like = PhotoLikes.objects.get(pk=pk, user=request.user)
    pet_photo_like = PhotoLikes.objects.filter(pet_photo_id=pk).first()
    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLikes.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f'#photo-{pk}')
