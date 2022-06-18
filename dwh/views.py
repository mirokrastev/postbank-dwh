from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from dwh.models import BankEmployee, POSTerminal, Trader
from dwh.serializers import POSTerminalSerializer, TraderSerializer, BankEmployeeSerializer


class BaseDataView(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        queryset.update(is_processed=True)
        return Response(data)


class SendTerminalDataView(BaseDataView):
    serializer_class = POSTerminalSerializer
    queryset = POSTerminal.objects.filter(is_processed=False)


class SendTraderDataView(BaseDataView):
    serializer_class = TraderSerializer
    queryset = Trader.objects.filter(is_processed=False)


class SendEmployeeDataView(BaseDataView):
    serializer_class = BankEmployeeSerializer
    queryset = BankEmployee.objects.filter(is_processed=False)
