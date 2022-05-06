from django.urls import path
from .views import lead_create, lead_delete, lead_details, lead_list, lead_update

urlpatterns = [
    path('',lead_list,name = "leads"),
    path('<int:pk>/',lead_details),
    path('<int:pk>/update/',lead_update),
    path('<int:pk>/delete/',lead_delete),
    path('new/',lead_create)
]