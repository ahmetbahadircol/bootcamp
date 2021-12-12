from django_filters import rest_framework as filters
<<<<<<< HEAD
from django.utils.translation import gettext_lazy as _
from payments.models import *


class BankFilter(filters.FilterSet):
    """
    Bank Filter
    """
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = Bank
        fields = ["name"]


class BankAccountFilter(filters.FilterSet):
    """
    Bank Account Filter
    """
    name = filters.CharFilter(label=_("Name"), lookup_expr="icontains")

    class Meta:
        model = BankAccount
        fields = ["bank", "name", "iban"]
=======

from payments.models import BankAccount, Bank


class BankAccountFilter(filters.FilterSet):

    class Meta:
        model = BankAccount
        fields = ("bank", "name")


class BankFilter(filters.FilterSet):

    class Meta:
        model = Bank
        fields = ("name",)
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
