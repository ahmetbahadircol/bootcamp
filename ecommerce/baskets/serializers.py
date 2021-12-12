from rest_framework import serializers
<<<<<<< HEAD
from baskets.models import Basket, BasketItem
=======

from baskets.models import BasketItem, Basket
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer


<<<<<<< HEAD
class BasketSerializer(serializers.ModelSerializer):
    """
    Basket Serializer
    """
    class Meta:
        model = Basket
        fields = ["customer", "status"]


class BasketItemSerializer(serializers.ModelSerializer):
    """
    Basket Item Serializer
    """
    class Meta:
        model = BasketItem
        fields = ["basket", "product", "quantity", "price"]


class BasketDetailedSerializer(serializers.ModelSerializer):
    """
    Basket Detailed Serializer for Customer
    """
    customer = CustomerSerializer()  # TODO: Add Customer Serializer!

    class Meta:
        model = Basket
        fields = ["customer", "status"]


class BasketItemDetailedSerializer(serializers.ModelSerializer):
    """
    Basket Item Detailed Serializer for Product and Basket
    """
    basket = BasketSerializer()
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = ["basket", "product", "quantity", "price"]
=======
class BasketItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketItem
        fields = ("id", "basket", "product", "quantity", "price")


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ("id", "customer", "status")


class BasketItemDetailedSerializer(BasketItemSerializer):
    basket = BasketSerializer()
    product = ProductSerializer()


class BasketDetailedSerializer(BasketSerializer):
    customer = CustomerSerializer()
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
