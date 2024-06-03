import django_filters
from django.forms import Form
from .models import Livre


class LivreFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(lookup_expr='icontains', label='titre')
    auteur = django_filters.CharFilter(lookup_expr='icontains', label='auteur')

    class Meta:
        model = Livre
        fields = ['titre','auteur']
        exclude = ['image_covr']
