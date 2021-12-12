from django_filters import rest_framework as filters
<<<<<<< HEAD
from django.utils.translation import gettext_lazy as _
from orders.models import *


class BillingAddressFilter(filters.FilterSet):
    """
    Billing Address Filter
    """
    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line_1 = filters.CharFilter(label=_("Address Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Address Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    city = filters.CharFilter(label=_("City"), lookup_expr="icontains")

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2",
                  "phone", "district", "zipcode", "city")


class ShippingAddressFilter(filters.FilterSet):
    """
    Billing Address Filter
    """
    full_name = filters.CharFilter(label=_("Full Name"), lookup_expr="icontains")
    line_1 = filters.CharFilter(label=_("Address Line 1"), lookup_expr="icontains")
    line_2 = filters.CharFilter(label=_("Address Line 2"), lookup_expr="icontains")
    district = filters.CharFilter(label=_("District"), lookup_expr="icontains")
    city = filters.CharFilter(label=_("City"), lookup_expr="icontains")

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2",
                  "phone", "district", "zipcode", "city")


class OrderBankAccountFilter(filters.FilterSet):
    """
    Order Bank Account Filter
    """
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")
    iban = filters.CharFilter(label=_("IBAN"), lookup_expr="icontains")
    bank_name = filters.CharFilter(label=_("Bank Name"), lookup_expr="icontains")

    class Meta:
        model = OrderBankAccount
        fields = ["name", "iban", "bank_name", "order"]


class OrderFilter(filters.FilterSet):
    """
    Order Filter
    """
    class Meta:
        model = Order
        fields = ["customer", "basket", "status"]


class OrderItemFilter(filters.FilterSet):
    """
    Order Item Filter
    """
    class Meta:
        model = OrderItem
        fields = ["order", "product", "price"]
=======

from orders.models import OrderItem, Order, OrderBankAccount, ShippingAddress, BillingAddress


class OrderItemFilter(filters.FilterSet):

    class Meta:
        model = OrderItem
        fields = ("order", "product")


class OrderFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields = ("customer", "status")


class BillingAddressFilter(filters.FilterSet):

    class Meta:
        model = BillingAddress
        fields = ("full_name", "city")


class ShippingAddressFilter(filters.FilterSet):

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "city")


class OrderBankAccountFilter(filters.FilterSet):

    class Meta:
        model = OrderBankAccount
        fields = ("name", "bank_name", "order")
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
