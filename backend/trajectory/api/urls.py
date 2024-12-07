from django.urls import path
from .views import DataProcessingView

urlpatterns = [
    path('api/', DataProcessingView.as_view(), name='data-process'),
]