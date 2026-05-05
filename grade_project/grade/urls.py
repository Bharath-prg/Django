from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_student),
    path('update/', views.update_grade),
    path('view/', views.view_students),
]