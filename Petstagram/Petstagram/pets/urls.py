from django.urls import path, include
from Petstagram.pets import views


urlpatterns = (
    path('pets/add/', views.add_pet, name='add-pet'),
    path('pets/<str:username>/pet/<slug:pet_slug>/', include(
        [
            path('edit/', views.edit_pet, name='edit-pet'),
            path('', views.details_pet, name='details-pet'),
            path('delete/', views.delete_pet, name='delete-pet'),
        ]
    )),

)