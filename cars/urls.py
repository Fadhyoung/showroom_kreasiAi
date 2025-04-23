from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('car/add/', views.car_add, name='car_add'),
    path('car/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('service/add/', views.service_add, name='service_add'),
]
