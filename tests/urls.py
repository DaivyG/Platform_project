from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('check-answer/', views.check_answer, name='check_answer')
]