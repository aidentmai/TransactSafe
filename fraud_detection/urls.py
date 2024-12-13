from django.urls import path
from . import views
from .views import preprocess_file

urlpatterns = [
    path('', views.index),
    path('preprocess/', preprocess_file, name='preprocess_file'),
]