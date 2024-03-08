from django.urls import path,include
from petstagram.accounts import views
from petstagram.accounts.views import SignInUserView, SignUpUserView

urlpatterns = (
    path('register/', SignUpUserView.as_view(), name='register'),
    path('login/', SignInUserView.as_view(), name='login'),
    path('profile/<int:pk>/', include(
        [
        path('', views.show_profile, name='show-profile'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),
        path('logout/', views.logout, name='logout'),
        ]


    )),
)