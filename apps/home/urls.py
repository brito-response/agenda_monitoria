from django.urls import path
from .views import home

urlpatterns = [
    path("<str:pessoa>/<int:idade>", home, name="home"),
]
