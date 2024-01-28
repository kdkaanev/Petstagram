from django.urls import path,include
from Petstagram.accounts import views



urlpatterns = (
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>', include(
        [
        path('', views.show_profile, name='show-profile'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),]


    )),
)