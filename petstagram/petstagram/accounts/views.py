

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.models import PetstagramUser


class PetstagrmaUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('email',)

class SignUpUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = PetstagrmaUserCreationForm
    success_url = reverse_lazy('index')

# Create your views here.
class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    redirect_authenticated_user = True
def register(request):
    context = {

    }
    return render(request, 'accounts/register-page.html', context)




def show_profile(request,pk):
    context = {

    }
    return render(request, 'accounts/profile-details-page.html', context)


def edit_profile(request, pk):
    context = {

    }
    return render(request, 'accounts/profile-edit-page.html', context)


def delete_profile(request, pk):
    context = {

    }
    return render(request, 'accounts/profile-delete-page.html', context)
def logout(request,pk):
    return redirect('logout')