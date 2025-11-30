from django.urls import path
from .views import *
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('profile/',p_list.as_view(),name="p_list"),
    path('profile/<int:id>/',p_detale.as_view(),name='p_detale'),
]