from django.urls import path, include
from petstagram.pets import views


urlpatterns = (
    path('add/', views.AddPetView.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include(
        [
            path('edit/', views.EditPetView.as_view(), name='edit-pet'),
            path('', views.DetailsPetView.as_view(), name='details-pet'),
            path('delete/',views.delete_pet, name='delete-pet'),
        ]
    )),

)
