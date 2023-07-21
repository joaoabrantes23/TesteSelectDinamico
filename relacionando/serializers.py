from rest_framework import serializers
from .models import Ods, Unidade, Cronograma

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'

class OdsSerializer(serializers.ModelSerializer):
    unidades = UnidadeSerializer(many=True, read_only=True)

    class Meta:
        model = Ods
        fields = '__all__'

    def get_unidades_caixa(self, obj):
        unidades = obj.unidades.all()
        return [(unidade.id, unidade.unidade_caixa) for unidade in unidades]
    
class CronogramaSerializer(serializers.ModelSerializer):
    unidades_disponiveis = serializers.SerializerMethodField()

    class Meta:
        model = Cronograma
        fields = '__all__'

    def get_unidades_disponiveis(self, obj):
        if obj.ods:
            unidades_da_ods = obj.ods.unidades.all()
            return [unidade.unidade_caixa for unidade in unidades_da_ods]
        return []
    unidade = serializers.ChoiceField(choices=[], write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'context' in kwargs:
            request = kwargs['context']['request']
            ods_id = request.data.get('ods') if request.method == 'POST' else None

            if ods_id is not None:
                unidades_da_ods = Unidade.objects.filter(ods=ods_id)
                unidades_disponiveis = [(unidade.unidade_caixa, unidade.unidade_caixa) for unidade in unidades_da_ods]
                self.fields['unidade'].choices = unidades_disponiveis