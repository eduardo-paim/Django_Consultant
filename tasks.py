from celery import shared_task
from .models import Proposta
from .api_client import analisar_proposta

@shared_task
def enviar_para_analise(proposta_id):
    proposta = Proposta.objects.get(pk=proposta_id)
    resultado = analisar_proposta(proposta.campos)  # Chamar API de Análise de Crédito
    proposta.resultado_analise = resultado
    proposta.save()
