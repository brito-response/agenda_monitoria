from django.contrib import admin
from django.urls import path, include
from apps.user import urls as user_urls
from apps.monitor import urls as monitor_urls
from apps.horario import urls as horario_urls
from apps.agendamento import urls as agendamento_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include(user_urls)),
    path("monitores/", include(monitor_urls)),
    path("horarios/", include(horario_urls)),
    path("agendamentos/", include(agendamento_urls)),
]
