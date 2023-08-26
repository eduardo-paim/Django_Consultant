from django.db import models

class Proposta(models.Model):
    campos = models.JSONField()  # Campos flexíveis definidos pelo admin
    status = models.CharField(max_length=20, default='Aguardando')  # Status da proposta
    resultado_analise = models.CharField(max_length=20, blank=True, null=True)  # Resultado da análise

    def __str__(self):
        return f"Proposta {self.id}"
