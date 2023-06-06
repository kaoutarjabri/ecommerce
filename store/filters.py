import django_filters
from django_filters import DateFilter, CharFilter
from .models import *
from django import forms

class OrderFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name',label='' , lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'search-input'}))