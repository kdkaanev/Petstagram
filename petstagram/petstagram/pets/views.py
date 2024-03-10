from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from petstagram.core.view_mixin import OwnerRequiredMixin
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetBaseForm, PetDeleteForm
from petstagram.pets.models import Pet
from django.contrib.auth.mixins import LoginRequiredMixin



class AddPetView(LoginRequiredMixin,CreateView):
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse_lazy('details-pet', kwargs={'username': 'kancho', 'pet_slug': self.object.slug})

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.user = self.request.user
    #
    #     return super().form_valid(form)
    #

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form


class EditPetView(OwnerRequiredMixin,UpdateView):
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



class DetailsPetView(LoginRequiredMixin,DetailView):
    # model = Pet
    queryset = Pet.objects.all().prefetch_related('pet_photos')
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.pet_photos.all()
        return context


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         pet_form.save()
#         return redirect('index')
#     context = {
#         'pet_form': pet_form,
#         'username': username,
#         'pet': pet,
#
#     }
#     return render(request, 'pets/pet-delete-page.html', context)

class DeletePetView(OwnerRequiredMixin,DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('index')
    extra_context = {'username': 'kancho', }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = self.form_class(instance=self.object)
    #     context['form'] = form
    #     return context

    # def get_object(self, queryset=None):
    #     return Pet.objects.get(slug=self.kwargs['pet_slug'])
    #
    #
    #
    # def delete(self, request, *args, **kwargs):
    #     pet = self.get_object()
    #     pet.delete()
    #     return redirect('home')
