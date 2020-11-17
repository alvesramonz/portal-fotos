from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('approval/', views.approval, name="approval"),
    path('gallery/', views.gallery, name="gallery"),

    path('', views.uploadPhoto, name="home"),
    path('update_photo_state/<str:pk>/', views.updatePhotoState, name="update_photo_state"),
]
