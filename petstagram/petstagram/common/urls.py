from django.urls import path
from petstagram.common import views

urlpatterns = (

    path('', views.IndexView.as_view(), name='index'),
    path('pet_photo_like/<int:pk>/', views.like_pet_photo, name='like_pet_photo'),
)
