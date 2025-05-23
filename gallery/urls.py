from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.image_upload, name='image_upload'),
    path('', views.image_list, name='image_list'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
