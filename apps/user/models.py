from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    username = None  # remove username
    TIPO_CHOICES = [("ALUNO", "Aluno"),("MONITOR", "Monitor"),("PROFESSOR", "Professor"),("ADMIN", "Admin")]  # enum

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="ALUNO")
    matricula = models.CharField(max_length=20, blank=True, null=True)
    curso = models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.tipo})"

    class Meta:
        db_table = "tb_users"
