from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

URLPattern[
    path('', view.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreate/', views.restaurantCreate),
    path('categoryCreate/', views.categoryCreate),
]