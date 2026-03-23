from django.urls import path
from .views import user_create, user_detail, user_update, user_delete, user_list

urlpatterns = [
    path("", user_list, name="user_list"), 
    path("create/", user_create, name="user_create"), 
    path("<int:id>/", user_detail, name="user_detail"),
    path("<int:id>/edit/", user_update, name="user_update"),
    path("<int:id>/delete/", user_delete, name="user_delete"),
]
