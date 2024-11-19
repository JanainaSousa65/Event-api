from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError  # Para lançar exceções de validação
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Ou especifique os campos que deseja serializar

    def validate(self, data):
        # Validação de start_date e end_date
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if end_date < start_date:  # Verifica se a data final é anterior à data inicial
            raise ValidationError({"error": "A data de fim deve ser maior ou igual à data de início."})
        
        return data  # Retorna os dados validados

    def validate_name(self, name):   
        # Valida se já existe um evento com o mesmo nome
        if Event.objects.filter(name=name).exists():
            raise ValidationError("Já existe um evento com esse nome.")
        
        return name  # Retorna o nome validado
     


        