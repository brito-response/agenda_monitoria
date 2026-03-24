from django.db import models


# Create your models here.
class Horario(models.Model):
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    vagas_totais = models.IntegerField()
    
    #relationships
    monitor = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="horarios")
    disciplina = models.ForeignKey("disciplina.Disciplina", on_delete=models.CASCADE,related_name="horarios")

    class Meta:
        db_table = "tb_horarios"
