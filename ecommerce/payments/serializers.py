from rest_framework import serializers

<<<<<<< HEAD
from payments.models import Bank, BankAccount


class BankSerializer(serializers.ModelSerializer):
    """
    Bank Serializer
    """
    class Meta:
        model = Bank
        fields = ["name"]


class BankAccountSerializer(serializers.ModelSerializer):
    """
    Bank Account Serializer
    """
    class Meta:
        model = BankAccount
        fields = ["bank", "name", "iban"]


class BankAccountDetailedSerializer(serializers.ModelSerializer):
    """
    Detailed Bank Account Serializer
    """
    bank = BankSerializer

    class Meta:
        model = BankAccount
        fields = ["bank", "name", "iban"]
        
=======
from payments.models import BankAccount, Bank


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ("id", "bank", "name", "iban")


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ("id", "name")


class BankAccountDetailedSerializer(BankAccountSerializer):
    bank = BankSerializer()
>>>>>>> 3ae8a86dc6e9202ccbccfd600c5859e6d6e3412d
