from django.urls import path
from .views import CandlestickData, LineChartData, BarChartData, PieChartData

urlpatterns = [
    path('candlestick-data/', CandlestickData.as_view()),
    path('line-chart-data/', LineChartData.as_view()),
    path('bar-chart-data/', BarChartData.as_view()),
    path('pie-chart-data/', PieChartData.as_view()),
]
