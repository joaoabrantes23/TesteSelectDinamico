from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# models.py

from django.db import models

class Ods(models.Model):
    numero_oes = models.CharField(max_length=100)

    def __str__(self):
        return f"Ordem de serviço {self.numero_oes}"
    

class Unidade(models.Model):
    ods = models.ForeignKey(Ods, related_name='unidades', on_delete=models.CASCADE)
    unidade_caixa = models.CharField(max_length=100)

    def __str__(self):
        return f"Unidade {self.id}"
    
class Cronograma(models.Model):
    ods = models.ForeignKey(Ods, on_delete=models.CASCADE)
    