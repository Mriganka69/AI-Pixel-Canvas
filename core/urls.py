from django.urls import path
from . import views  # assuming you have a views.py with a 'home' view

urlpatterns = [
    path('', views.home, name='home'),  # or any other path/view you use
]
