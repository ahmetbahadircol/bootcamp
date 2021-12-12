from rest_framework import viewsets

<<<<<<< HEAD
from baskets.filters import BasketFilter
from core.mixins import DetailedViewSetMixin
from baskets.serializers import *


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    """
    Detailed ViewSet for Basket
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter  # TODO: basket için filter ekle
=======
from baskets.filters import BasketItemFilter, BasketFilter
from baskets.models import BasketItem, Basket
from baskets.serializers import BasketItemSerializer, BasketSerializer, BasketItemDetailedSerializer, BasketDetailedSerializer
from core.mixins import DetailedViewSetMixin


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketItemFilter
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }


class BasketViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filterset_class = BasketFilter
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
    serializer_action_classes = {
        "detailed_list": BasketDetailedSerializer,
        "detailed": BasketDetailedSerializer,
    }
<<<<<<< HEAD


class BasketItemViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    """
    Detailed ViewSet for BasketItem
    """
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filterset_class = BasketFilter  # TODO: basketitem için filter ekle
    serializer_action_classes = {
        "detailed_list": BasketItemDetailedSerializer,
        "detailed": BasketItemDetailedSerializer,
    }
=======
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
