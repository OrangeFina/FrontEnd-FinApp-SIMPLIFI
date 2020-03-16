from django.urls import path
from . import views


urlpatterns = [
    path('risk-list', views.risk_list, name='risk_list'),
]