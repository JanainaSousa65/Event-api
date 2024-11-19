from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from proj.models import Event
from proj.serializers import EventSerializer

def home(request):
    return HttpResponse("Bem-vindo")

@api_view(['POST'])
def evento_create(request):
    # Recebe os dados da requisição
    serializer = EventSerializer(data=request.data)  # Corrigido para request.data
    if serializer.is_valid():
        serializer.save()  # Salva o evento
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna sucesso
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Corrigido para HTTP_400_BAD_REQUEST

@api_view(['GET'])
def event_list(request): 
    # GET - para listar todos os eventos cadastrados
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
