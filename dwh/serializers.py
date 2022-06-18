from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from dwh.models import Trader, BankEmployee, POSTerminal
from accounts.serializers import UserSerializer


class AdditionalTraderSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = Trader
        fields = ('phone_number',)


class TraderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    additional_info = serializers.SerializerMethodField()

    def get_additional_info(self, instance):
        return AdditionalTraderSerializer(instance).data

    class Meta:
        model = Trader
        fields = ('id', 'user', 'additional_info', 'created_at', 'modified_at')


class BankEmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BankEmployee
        fields = ('id', 'user', 'created_at', 'modified_at')


class POSTerminalSerializer(serializers.ModelSerializer):
    trader = TraderSerializer()

    class Meta:
        model = POSTerminal
        fields = ('id', 'trader', 'created_at', 'modified_at')
