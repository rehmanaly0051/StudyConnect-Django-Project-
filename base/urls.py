from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('search/', views.search_rooms, name='search-rooms'),
    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name = 'create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path("delete-message/<str:pk>/", views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name='update-user'),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
