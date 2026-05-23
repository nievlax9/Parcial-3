from rest_framework import viewsets, filters,generics
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .models import personajes
from .serializers import PersonajesSerializer,RegisterSerializer
from .filters import personajeFilter

# Create your views here.
class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = personajes.objects.all()  # Queries que define todos los carros disponibles
    serializer_class = PersonajesSerializer  # Serializador que se usará para este modelo

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_class = personajeFilter

    ordering_fields = ['nombre','casa','estado']

# RegisterView es la vista para el registro de usuarios
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
