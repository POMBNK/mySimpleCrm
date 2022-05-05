from django.urls import path
from .views import lead_create, lead_details, lead_list

urlpatterns = [
    path('',lead_list,name = "pisya"),
    path('<int:pk>/',lead_details),
    path('new/',lead_create)
]