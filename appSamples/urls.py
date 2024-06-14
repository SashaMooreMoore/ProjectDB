from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="urlHomePage"),
    path('condition', views.ConditionPage.as_view(), name="urlConditionPage"),
]

