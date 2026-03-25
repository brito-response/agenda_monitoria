from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ["data", "hora_inicio", "hora_fim", "vagas_totais", "disciplina"]