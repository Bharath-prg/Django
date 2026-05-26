from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('add_student/',views.add_student),
    path('delete_student/',views.delete_student)
]