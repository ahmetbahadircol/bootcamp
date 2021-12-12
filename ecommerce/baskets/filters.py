<<<<<<< HEAD
from django.db.models import Q
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _

from baskets.models import Basket, BasketItem


class BasketFilter(filters.FilterSet):
    customer = filters.CharFilter(label=_("Customer"), method="filter_name")

    class Meta:
        model = Basket
        fields = ("customer", "status")

    @staticmethod
    def filter_name(self, qs, name, value):
        return qs.filter(customer__first_name__icontains=value)


class BasketItemFilter(filters.FilterSet):
    product = filters.CharFilter(label=_("Product"), method="filter_name")

    class Meta:
        model = BasketItem
        fields = ("basket", "product", "quantity", "price")

=======
from django_filters import rest_framework as filters

from baskets.models import BasketItem, Basket


class BasketItemFilter(filters.FilterSet):

    class Meta:
        model = BasketItem
        fields = ("product", "quantity", "price")


class BasketFilter(filters.FilterSet):

    class Meta:
        model = Basket
        fields = ("customer", "status")
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
