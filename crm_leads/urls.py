from django.urls import path
from .views import lead_create, lead_details, lead_list, lead_update

urlpatterns = [
    path('',lead_list,name = "leads"),
    path('<int:pk>/',lead_details),
    path('<int:pk>/update/',lead_update),
    path('new/',lead_create)
]