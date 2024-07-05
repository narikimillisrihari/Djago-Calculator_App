from django.urls import path
from calculator_app import views

urlpatterns = [
    path('main/', views.home, name="home"),
    path('clear/',views.clear, name="clear"),
]
