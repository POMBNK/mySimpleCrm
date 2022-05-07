from django.urls import path
from .views import lead_create, lead_delete, lead_details, lead_list, lead_update

app_name = "leads"

urlpatterns = [
    path('',lead_list,name="lead-list"),
    path('<int:pk>/',lead_details,name="details"),
    path('<int:pk>/update/',lead_update,name="update"),
    path('<int:pk>/delete/',lead_delete,name="delete"),
    path('new/',lead_create,name="create")
]