from rest_framework import routers
from .views import OdsViewSet, UnidadeViewSet, CronogramaViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register(r'ods', OdsViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'cronograma', CronogramaViewSet)


urlpatterns = router.urls