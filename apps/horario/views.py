from django.shortcuts import get_object_or_404, render, redirect
from apps.horario.forms import HorarioForm
from core.decorators import acesso_required
from .models import Horario
from apps.agendamento.models import Agendamento


# Create your views here.
def horario_list(request):
    horarios = Horario.objects.all()
    return render(request, "horario/list.html", {"horarios": horarios})


@acesso_required(tipos=["MONITOR"], permissoes=["users.view_user"])
def horario_create(request):
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            horario = form.save(commit=False)
            horario.monitor = request.user
            horario.save()
            return redirect("/horarios/")
    else:
        form = HorarioForm()

    return render(request, "horario/create.html", {"form": form})


@acesso_required(tipos=["MONITOR", "ADMIN"], permissoes=["users.view_user"])
def horario_delete(request, id):
    horario = get_object_or_404(Horario, id=id)

    if request.user != horario.monitor and request.user.tipo != "ADMIN":
        return redirect("/horarios/")

    horario.delete()
    return redirect("/horarios/")


def horario_detail(request, id):
    horario = get_object_or_404(Horario, id=id)
    agendamentos = Agendamento.objects.filter(horario=horario)

    return render(
        request,
        "horario/detail.html",
        {"horario": horario, "agendamentos": agendamentos},
    )
