from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Proposta
from .serializers import PropostaSerializer

@api_view(['POST'])
def criar_proposta(request):
    serializer = PropostaSerializer(data=request.data)
    if serializer.is_valid():
        proposta = serializer.save()
        # Enviar proposta para análise assíncrona com Celery
        enviar_para_analise.delay(proposta.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
