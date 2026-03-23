from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    TIPO_CHOICES = [("ALUNO", "Aluno"),("MONITOR", "Monitor"),("PROFESSOR", "Professor"),("ADMIN", "Admin")] # enum
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="ALUNO")
    matricula = models.CharField(max_length=20, blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.tipo})"
    
    class Meta:
        db_table = "tb_users"
