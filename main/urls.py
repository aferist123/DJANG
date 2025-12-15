from django.urls import path
from . import views

urlpatterns = [
    # Коли хтось заходить на головну сторінку, викликаємо функцію index
    path('', views.index, name='home'),]