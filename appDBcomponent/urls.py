from django.urls import path
from . import views

urlpatterns = [
    path('all', views.RequestDBAll.as_view(), name='urlRequestDBAll'),
    path('filter', views.RequestDbFilter.as_view(), name='urlRequestDbFilter'),
    path('get', views.RequestDbGet.as_view(), name='urlRequestDbGet'),
    path('create', views.RequestDbCreate.as_view(), name='urlRequestDbCreate'),
    path('update-one', views.RequestDbUpdateOne.as_view(), name='urlRequestDbUpdateOne'),
    path('update-two', views.RequestDbUpdateTwo.as_view(), name='urlRequestDbUpdateTwo'),
    path('update-three', views.RequestDbUpdateThree.as_view(), name='urlRequestDbUpdateThree'),
    path('update-four', views.RequestDbUpdateFour.as_view(), name='urlRequestDbUpdateFour'),
    path('update-get', views.RequestDbUpdateGet.as_view(), name='urlRequestDbUpdateGet'),
    path('delete', views.RequestDbDelete.as_view(), name='urlRequestDbDelete'),
]