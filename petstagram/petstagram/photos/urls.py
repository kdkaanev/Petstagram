from django.urls import path, include

from petstagram.photos import views

urlpatterns = (
    path('add/', views.PetPhotoCreateView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('edit/', views.EditPhotoView.as_view(), name='edit-photo'),
        path('', views.DetailsPhotoView.as_view(), name='details-photo'),]
    )),
)
