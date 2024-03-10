from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.core.view_mixin import OwnerRequiredMixin
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import PetPhoto
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class PetPhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    queryset = PetPhoto.objects.all().prefetch_related('pets')

    def get_success_url(self):
        return reverse('details-photo', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form



class EditPhotoView(OwnerRequiredMixin,UpdateView):
    queryset = PetPhoto.objects.all()
    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm

    def get_success_url(self):
        return reverse('details-photo', kwargs={'pk': self.object.pk})



class DetailsPhotoView(LoginRequiredMixin,DetailView):
    queryset = PetPhoto.objects.all().prefetch_related('likes').prefetch_related('comments').prefetch_related('pets')
    template_name = 'photos/photo-details-page.html'
