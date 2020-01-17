from django.urls import path

from .views import CustomerListAPIView, CustomerDetailView, CustomerCreateAPIView

urlpatterns = [
    path('customer/create/', CustomerCreateAPIView.as_view()),
    path('customer/all/', CustomerListAPIView.as_view()),
    path('customer/detail/<int:pk>/', CustomerDetailView.as_view()),
]
