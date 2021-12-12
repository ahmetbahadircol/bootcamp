from rest_framework import viewsets
<<<<<<< HEAD

from core.mixins import DetailedViewSetMixin
# from products.filters import ProductFilter
from customers.models import Customer
from customers.serializers import *


class CustomerViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # filterset_class = ProductFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressDetailedSerializer
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }
=======

from core.mixins import DetailedViewSetMixin
from customers.filters import CustomerFilter, AddressFilter, CountryFilter, CityFilter
from customers.models import Customer, Address, City, Country
from customers.serializers import CustomerSerializer, AddressSerializer, CitySerializer, CountrySerializer, \
    AddressDetailedSerializer, CityDetailedSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter


class CityViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter
    serializer_action_classes = {
        "detailed_list": CityDetailedSerializer,
        "detailed": CityDetailedSerializer,
    }


class AddressViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilter
    serializer_action_classes = {
        "detailed_list": AddressDetailedSerializer,
        "detailed": AddressDetailedSerializer,
    }


>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
