from django.urls import path
from .views import (HorarioListView,HorarioCreateView,HorarioDeleteView,HorarioDetailView)

urlpatterns = [
    path("", HorarioListView.as_view(), name="horario_list"),
    path("create/", HorarioCreateView.as_view(), name="horario_create"),
    path("<int:id>/delete/", HorarioDeleteView.as_view(), name="horario_delete"),
    path("<int:id>/", HorarioDetailView.as_view(), name="horario_detail"),
]
