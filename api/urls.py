from django.urls import path
from .views import process_data, operation_code, index

urlpatterns = [
    path('bfhl/', process_data),
    path('bfhl/get/', operation_code),
    path('frontend/', index),
]
