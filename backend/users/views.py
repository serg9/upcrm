from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Customer
from .serialisers import CustomerSerializer


class CustomerCreateAPIView(CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
