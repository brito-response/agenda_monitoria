from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from apps.horario.forms import HorarioForm
from core.decorators import acesso_required
from .models import Horario
from apps.agendamento.models import Agendamento

class HorarioListView(ListView):
    model = Horario
    template_name = "horario/list.html"
    context_object_name = "horarios"
    
@method_decorator(acesso_required(tipos=["MONITOR"], permissoes=["users.view_user"]),name="dispatch")
class HorarioCreateView(CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = "horario/create.html"
    success_url = "/horarios/"

    def form_valid(self, form):
        horario = form.save(commit=False)
        horario.monitor = self.request.user
        horario.save()
        return redirect(self.success_url)
    

@method_decorator(acesso_required(tipos=["MONITOR", "ADMIN"], permissoes=["users.view_user"]),name="dispatch")
class HorarioDeleteView(DeleteView):
    model = Horario
    success_url = "/horarios/"
    pk_url_kwarg = "id"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.user != self.object.monitor and request.user.tipo != "ADMIN":
            return redirect("/horarios/")

        return super().dispatch(request, *args, **kwargs)
    

class HorarioDetailView(DetailView):
    model = Horario
    template_name = "horario/detail.html"
    context_object_name = "horario"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agendamentos"] = Agendamento.objects.filter(horario=self.object)
        return context