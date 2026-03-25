from django.http import HttpRequest, HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect
from typing import Callable, Iterable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R", bound=HttpResponse)


def acesso_required(tipos: list[str] | None = None, permissoes: Iterable[str] | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(view_func: Callable[P, R]) -> Callable[P, R]:
        def _wrapped_view(request: HttpRequest, *args: P.args, **kwargs: P.kwargs) -> R:
            user = request.user

            if not user.is_authenticated:
                return redirect("/") # type: ignore

            tem_tipo = False
            tem_permissao = False

            # verifica tipo
            if tipos:
                tem_tipo = user.tipo in tipos

            # verifica permissões
            if permissoes:
                tem_permissao = any(user.has_perm(p) for p in permissoes)

            if tipos or permissoes:
                if not (tem_tipo or tem_permissao):
                    return HttpResponseForbidden("Sem acesso")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
