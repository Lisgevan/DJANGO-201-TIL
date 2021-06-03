from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path('<str:username>/', views.ProfileDetailView.as_view(), name='detail'),
    path('<str:username>/follow/', views.FollowView.as_view(), name='follow'),
    path('<str:username>/profile/', views.UserProfileView.as_view(), name='profile'),
    path('<str:username>/manage/', views.ManageUserView.as_view(), name='manage'),
    path('<int:user_id>/avatar/', views.ManageProfileView.as_view(), name='avatar'),
]