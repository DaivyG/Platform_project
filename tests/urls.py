from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('check-answer/', views.check_answer, name='check_answer')
]