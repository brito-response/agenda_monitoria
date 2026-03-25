from django.urls import path
from .views import (agendar,cancelar_agendamento,meus_agendamentos,agendamentos_do_horario)

urlpatterns = [
    path("agendar/<int:horario_id>/", agendar),
    path("cancelar/<int:id>/", cancelar_agendamento),
    path("meus/", meus_agendamentos),
    path("horario/<int:horario_id>/", agendamentos_do_horario),
]
