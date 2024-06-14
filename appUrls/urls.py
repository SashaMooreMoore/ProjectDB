from django.urls import path
from . import views

urlpatterns = [
    path('static', views.StaticUrl.as_view(), name="urlStaticUrl"),
    path('dinamic-int-<int:number>', views.DinamicInt.as_view(), name="urlDinamicInt"),
    path('dinamic-slug-<slug:text>', views.DinamicSlug.as_view(), name="urlDinamicSlug"),
]