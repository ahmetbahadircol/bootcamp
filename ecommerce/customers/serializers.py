from rest_framework import serializers
<<<<<<< HEAD
from customers.models import Customer, Country, City, Address


class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer Serializer
    """
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email"]


class CountrySerializer(serializers.ModelSerializer):
    """
    Country Serializer
    """
    class Meta:
        model = Country
        fields = ["name"]


class CitySerializer(serializers.ModelSerializer):
    """
    City Serializer
    """
    class Meta:
        model = City
        fields = ["name", "country"]


class AddressSerializer(serializers.ModelSerializer):
    """
    Address Serializer
    """
    class Meta:
        model = Address
        fields = ["customer", "name", "full_name", "line1", "line2", "phone", "district", "zipcode", "city",
                  "is_default"]


class AddressDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Address Serializer
    """
    customer = CustomerSerializer()
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ["customer", "name", "full_name", "line1", "line2", "phone", "district", "zipcode", "city",
                  "is_default"]
=======

from customers.models import Customer, Address, City, Country


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ("id", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ("id", "name", "country")


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ("id", "customer", "name", "full_name", "line_1", "line_2", "phone", "district", "zipcode", "city", "is_default")


class AddressDetailedSerializer(AddressSerializer):
    customer = CustomerSerializer()
    city = CitySerializer()


class CityDetailedSerializer(CitySerializer):
    country = CountrySerializer()
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
