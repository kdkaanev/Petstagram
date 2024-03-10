
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms

from petstagram.accounts.forms import PetstagrmaUserCreationForm
from petstagram.accounts.models import Profile
from petstagram.photos.models import PetPhoto


class SignUpUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = PetstagrmaUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


# Create your views here.
class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True

class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = 'accounts/profile-details-page.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_photos'] = (
            PetPhoto.objects.
            filter(user_id=self.object.pk).
            order_by('-created_at')
        )
        return context


class ProfilUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-edit-page.html'
    fields = ('first_name', 'last_name', 'profile_picture', 'date_of_birth')



    def get_success_url(self):
        return reverse_lazy('show-profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-delete-page.html'
# def edit_profile(request, pk):
#     context = {
#
#     }
#     return render(request, 'accounts/profile-edit-page.html', context)


# def delete_profile(request, pk):
#     context = {
#
#     }
#     return render(request, 'accounts/profile-delete-page.html', context)
def signout(request):
    logout(request)
    return redirect('index')