from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SertifikatViewSet

router = DefaultRouter()
router.register(r'sertifikatlar', SertifikatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]