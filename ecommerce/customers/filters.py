<<<<<<< HEAD
from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from customers.models import Customer


class CustomerFilter(filters.FilterSet):
    name = filters.CharFilter(label=_("First Name"), method="filter_name")

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email")

    def filter_name(self, qs, name, value):
        replaced_value = value.replace("Ş", "ş")
        return qs.filter(Q(first_name__icontains=replaced_value) | Q(first_name__icontains=value))
=======
from django_filters import rest_framework as filters

from customers.models import Customer, Address, City, Country


class CustomerFilter(filters.FilterSet):

    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "is_active")


class AddressFilter(filters.FilterSet):

    class Meta:
        model = Address
        fields = ("customer", "name", "city")


class CityFilter(filters.FilterSet):

    class Meta:
        model = City
        fields = ("name", "country")


class CountryFilter(filters.FilterSet):

    class Meta:
        model = Country
        fields = ("name",)
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
