from rest_framework import viewsets
<<<<<<< HEAD
from core.mixins import DetailedViewSetMixin
from payments.filters import BankFilter, BankAccountFilter
from payments.models import Bank, BankAccount
from payments.serializers import BankSerializer, BankAccountSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter


class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": "BankAccountDetailedSerializer",
        "detailed": "BankAccountDetailedSerializer"
    }
=======

from core.mixins import DetailedViewSetMixin
from payments.filters import BankAccountFilter, BankFilter
from payments.models import BankAccount, Bank
from payments.serializers import BankAccountSerializer, BankSerializer, BankAccountDetailedSerializer


class BankAccountViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    filterset_class = BankAccountFilter
    serializer_action_classes = {
        "detailed_list": BankAccountDetailedSerializer,
        "detailed": BankAccountDetailedSerializer,
    }


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filterset_class = BankFilter

>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
