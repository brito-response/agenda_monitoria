from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreateForm
from .models import User

# Create your views here.

def user_list(request):
    users = User.objects.all()
    return render(request, "user/list.html", {"users": users})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "user/detail.html", {"user": user})


def user_create(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("user_list")
    else:
        form = UserCreateForm()

    return render(request, "user/create.html", {"form": form})


def user_update(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.tipo = request.POST.get("tipo")

        user.save()
        return redirect("user_list")

    return render(request, "user/update.html", {"user": user})


def user_delete(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.delete()
        return redirect("user_list")

    return render(request, "user/delete.html", {"user": user})