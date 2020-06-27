from . import views
from .views import SignupView
from django.urls import path

urlpatterns = [

    path('signup/', views.SignupView.as_view(), name='signup')
]
