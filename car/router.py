from carapi.viewsets import CarViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('car',CarViewset)