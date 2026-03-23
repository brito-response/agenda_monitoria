from django.contrib import admin
from django.urls import path, include
from apps.user import urls as user_urls
from apps.monitor import urls as monitor_urls
from apps.horario import urls as horario_urls
from apps.agendamento import urls as agendamento_urls
from apps.home import urls as home_urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include(home_urls)),
    path("users/", include(user_urls)),
    path("monitores/", include(monitor_urls)),
    path("horarios/", include(horario_urls)),
    path("agendamentos/", include(agendamento_urls)),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
