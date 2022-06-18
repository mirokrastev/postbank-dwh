from django.contrib import admin

from dwh.models import Trader, POSTerminal, BankEmployee

admin.site.register(Trader)
admin.site.register(POSTerminal)
admin.site.register(BankEmployee)
