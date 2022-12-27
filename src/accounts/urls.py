from . import views
from django.urls import path, include

urlpatterns = [
    path('register/', views.SignUp.as_view(), name="registro"),
]
