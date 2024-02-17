from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetBaseForm,PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse_lazy('details-pet', kwargs={'username': 'kancho', 'pet_slug': self.object.slug})


class EditPetView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'kancho'
        return context


    def get_success_url(self):
        return reverse_lazy('details-pet', kwargs={
            'username': self.request.GET.get('username'),
            'pet_slug': self.object.slug
        }

         )





class DetailsPetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.pet_photos.all()
        return context


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet_form.save()
        return redirect('index')
    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,

    }
    return render(request, 'pets/pet-delete-page.html', context)

# class DeletePetView(DeleteView):
#     model = Pet
#     template_name = 'pets/pet-delete-page.html'
#
#     slug_url_kwarg = 'pet_slug'
#
#
#
#     def get_object(self, queryset=None):
#         return Pet.objects.get(slug=self.kwargs['pet_slug'])
#
#
#
#     def delete(self, request, *args, **kwargs):
#         pet = self.get_object()
#         pet.delete()
#         return redirect('home')

