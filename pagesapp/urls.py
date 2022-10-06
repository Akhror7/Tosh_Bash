from django.urls import path
from .views import formInfo,predictor

urlpatterns = [
    path('',predictor,name='home'),
    path('result',formInfo,name='result')
]