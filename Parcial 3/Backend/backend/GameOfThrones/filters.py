import django_filters
from .models import personajes

class personajeFilter(django_filters.FilterSet):  
    
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')  
    casa = django_filters.CharFilter(field_name='casa', lookup_expr='icontains')
    estado = django_filters.CharFilter(field_name='estado', lookup_expr='icontains')
    
    class Meta:  
        model = personajes
        fields = ['nombre', 'casa', 'estado']  