from django.db import models


# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)

    class Meta:
        db_table = "tb_disciplinas"
