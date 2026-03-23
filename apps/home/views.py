from django.shortcuts import render

# from django.http import HttpResponse


def home(request, pessoa: str, idade: int):
    return render(request, "index.html", {"v_nome": pessoa, "v_idade": idade})  # passamos parametros como dicionario
