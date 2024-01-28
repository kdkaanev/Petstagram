from django.urls import path, include

from Petstagram.photos import views

urlpatterns = (
    path('photos/add/', views.add_photo, name='add-photo'),
    path('photos/<int:pk>', include([
        path('edit/', views.edit_photo, name='edit-photo'),
        path(' ', views.details_photo, name='details-photo'),]
    )),
)