from django.contrib import admin
from django.urls import path
from website import views
from .import billingapi

urlpatterns = [
    path('anuj',views.index),
    path('anup/',billingapi.employeeAPI.as_view()),
    path('anup/<int:pk>/',billingapi.employeeAPI.as_view()),
]