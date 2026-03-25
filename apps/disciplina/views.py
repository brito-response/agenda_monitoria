from django.shortcuts import get_object_or_404, render, redirect
from core.decorators import acesso_required
from .models import Disciplina

# Create your views here.


@acesso_required(
    tipos=["PROFESSOR", "ADMIN", "MONITOR"], permissoes=["users.view_user"]
)
def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    return render(request, "disciplina/list.html", {"disciplinas": disciplinas})


def disciplina_create(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        Disciplina.objects.create(nome=nome)
        return redirect("/disciplinas/")

    return render(request, "disciplina/create.html")


def disciplina_update(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == "POST":
        disciplina.nome = request.POST.get("nome")
        disciplina.save()
        return redirect("/disciplinas/")

    return render(request, "disciplina/update.html", {"disciplina": disciplina})


def disciplina_delete(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    disciplina.delete()
    return redirect("/disciplinas/")
