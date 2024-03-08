from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('universities/', views.university_list, name='university_list'),
    path('universities/<int:university_id>/', views.discipline_list, name='discipline_list'),
     path('start/', views.start, name='start'),
]