from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import User
from base.models import BaseModel


class Trader(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    phone_number = PhoneNumberField()
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'Trader<{self.user.username}>'


class POSTerminal(BaseModel):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name='pos_terminals')
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.trader.user.username}'


class BankEmployee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'Employee<{self.user.username}>'
