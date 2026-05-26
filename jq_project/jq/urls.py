from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('add_feedback/',views.add_feedback)]