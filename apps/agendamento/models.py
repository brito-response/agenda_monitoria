from django.db import models


# Create your models here.
class Agendamento(models.Model):
    status = models.CharField(max_length=20)
    data_agendamento = models.DateTimeField(auto_now_add=True)

    #relationships
    aluno = models.ForeignKey("user.User", on_delete=models.CASCADE,related_name="agendamentos")
    horario = models.ForeignKey("horario.Horario", on_delete=models.CASCADE,related_name="agendamentos")
    
    class Meta:
        db_table = "tb_agendamentos"
