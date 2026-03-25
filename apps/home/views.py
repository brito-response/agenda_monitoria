from django.shortcuts import render
from datetime import datetime
from core.decorators import acesso_required


def home(request):
    return render(request, "index.html", {"data": datetime.now()})


@acesso_required(tipos=["ALUNO", "PROFESSOR","ADMIN","MONITOR"], permissoes=["users.view_user"])
def manager(request):
    return render(request, "manager.html", {"data": datetime.now()})
