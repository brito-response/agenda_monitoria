from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from core.decorators import acesso_required
from .models import Agendamento
from apps.horario.models import Horario


# Create your views here.
@acesso_required(tipos=["ALUNO"], permissoes=[])
def agendar(request, horario_id):
    horario = get_object_or_404(Horario, id=horario_id)

    # evita duplicado
    if Agendamento.objects.filter(aluno=request.user, horario=horario).exists():
        return redirect("/horarios/")

    # regra de capacidade (se existir campo)
    if hasattr(horario, "capacidade"):
        if Agendamento.objects.filter(horario=horario).count() >= horario.capacidade:
            return HttpResponse("Horário lotado")

    Agendamento.objects.create(aluno=request.user, horario=horario)

    return redirect("/horarios/")


@acesso_required(tipos=["ALUNO"], permissoes=[])
def cancelar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if agendamento.aluno != request.user:
        return redirect("/horarios/")

    agendamento.delete()
    return redirect("/meus-agendamentos/")


@acesso_required(tipos=["ALUNO"], permissoes=[])
def meus_agendamentos(request):
    agendamentos = Agendamento.objects.filter(aluno=request.user)

    return render(request, "agendamento/meus.html", {"agendamentos": agendamentos})


def agendamentos_do_horario(request, horario_id):
    horario = get_object_or_404(Horario, id=horario_id)

    if request.user != horario.monitor and request.user.tipo != "ADMIN":
        return redirect("/horarios/")

    agendamentos = Agendamento.objects.filter(horario=horario)

    return render(request,"agendamento/list.html",{"horario": horario, "agendamentos": agendamentos})
