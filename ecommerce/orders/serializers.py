<<<<<<< HEAD
from django.db.transaction import atomic
from rest_framework import serializers

from baskets.serializers import BasketSerializer
from customers.serializers import CitySerializer, CustomerSerializer
from orders.models import *


class BillingAddressSerializer(serializers.ModelSerializer):
    """
    Billing Address Serializer
    """
    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):
    """
    Shipping Address Serializer
    """
    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderSerializer(serializers.ModelSerializer):
    """
    Order Serializer
    """
    class Meta:
        model = Order
        fields = ["customer", "basket", "status", "billing_address", "shipping_address", "total_price"]


class OrderBankAccountSerializer(serializers.ModelSerializer):
    """
    Order Bank Account Serializer
    """
    class Meta:
        model = OrderBankAccount
        fields = ["name", "iban", "bank_name", "order"]


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Order Item Serializer
    """
    class Meta:
        model = OrderItem
        fields = ["order", "product", "price"]


class BillingAddressDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Billing Address Serializer
    """
    city = CitySerializer

    class Meta:
        model = BillingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Shipping Address Serializer
    """
    city = CitySerializer

    class Meta:
        model = ShippingAddress
        fields = ("full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Order Serializer
    """
    customer = CustomerSerializer
    basket = BasketSerializer
    billing_address = BillingAddressSerializer
    shipping_address = ShippingAddressSerializer

    class Meta:
        model = Order
        fields = ["customer", "basket", "status", "billing_address", "shipping_address", "total_price"]


class OrderBankAccountDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Order Bank Account Serializer
    """
    order = OrderSerializer

    class Meta:
        model = OrderBankAccount
        fields = ["name", "iban", "bank_name", "order"]


class OrderItemDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Order Item Serializer
    """
    order = OrderSerializer

    class Meta:
        model = OrderItem
        fields = ["order", "product", "price"]
=======
from rest_framework import serializers

from baskets.serializers import BasketSerializer
from customers.serializers import CustomerSerializer, CitySerializer
from orders.models import OrderItem, Order, BillingAddress, ShippingAddress, OrderBankAccount


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "price")


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "customer", "basket", "status", "billing_address", "shipping_address", "total_price")


class BillingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class ShippingAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShippingAddress
        fields = ("id", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city")


class OrderBankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderBankAccount
        fields = ("id", "name", "iban", "bank_name", "order")


class OrderItemDetailedSerializer(OrderItemSerializer):
    order = OrderSerializer()


class OrderDetailedSerializer(OrderSerializer):
    customer = CustomerSerializer()
    basket = BasketSerializer()
    billing_address = BillingAddressSerializer()
    shipping_address = ShippingAddressSerializer()


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()


class BillingAddressDetailedSerializer(BillingAddressSerializer):
    city = CitySerializer()


class ShippingAddressDetailedSerializer(ShippingAddressSerializer):
    city = CitySerializer()


class OrderBankAccountDetailedSerializer(OrderBankAccountSerializer):
    order = OrderSerializer()
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
