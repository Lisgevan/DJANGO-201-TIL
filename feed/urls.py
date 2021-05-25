from django.urls import path

from . import views

app_name = "feed"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new/', views.CreateNewPost.as_view(), name='new_post'),
    path('myposts/', views.UserPosts.as_view(), name='user_posts'),
    path('followedby/', views.FollowedByPosts.as_view(), name='followedby_posts'),
]
