from django.urls import include, path
from .views import *
urlpatterns = [
    path('account/',include("django.contrib.auth.urls")),
    path('account/sign_in/',RegesterView.as_view(),name='sign_in' ),
    path('login',log_in_view.as_view(),name='login')
]