

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import PetstagrmaUserCreationForm
from petstagram.accounts.models import Profile


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

# def show_profile(request,pk):
#     context = {
#
#     }
#     return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    context = {

    }
    return render(request, 'accounts/profile-edit-page.html', context)


def delete_profile(request, pk):
    context = {

    }
    return render(request, 'accounts/profile-delete-page.html', context)
def signout(request):
    logout(request)
    return redirect('index')