from django.urls import path

from dwh import views


urlpatterns = [
    path('api/users/traders', views.SendTraderDataView.as_view(), name='traders'),
    path('api/users/bank-employees', views.SendEmployeeDataView.as_view(), name='bank-employees'),
    path('api/pos-terminals', views.SendTerminalDataView.as_view(), name='pos-terminals'),
]
