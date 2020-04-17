from django.urls import path
from . import views


urlpatterns = [
    path('risk-list', views.risk_list, name='risk_list'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('database', views.database, name="database"),
    path('allocation', views.allocation, name="allocation"),
    path('stockexplorer', views.stockexplorer, name="stockexplorer"),   
    path('stock-query', views.stock_query, name="stock_query"),
    path('chartdb', views.chartdatabase, name="chart_database")       
]