from django.urls import path
from .views import horario_list, horario_create, horario_detail, horario_delete

urlpatterns = [
    path("", horario_list, name="horarios"),
    path("create/", horario_create, name="create_horario"),
    path("<int:id>/", horario_detail, name="horario_detail"),
    path("<int:id>/delete/", horario_delete, name="horario_delete"),
]
