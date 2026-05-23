from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonajeViewSet,RegisterView


router = DefaultRouter()
router.register(r'Personaje',PersonajeViewSet)

# Incluir las URLs del enrutador en las rutas del proyecto
urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegisterView.as_view(),name='register')
]