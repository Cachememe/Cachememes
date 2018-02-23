from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),

    path('<int:from_nr>/get_more_memes/', views.get_more_memes, name='get_more_memes'),

    path('<int:from_nr>/get_more_canvas_memes/', views.get_more_canvas_memes, name='get_more_canvas_memes'),
]
