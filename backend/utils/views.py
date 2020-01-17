from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Enum
from .serialisers import EnumSerializer


class EnumCreateAPIView(CreateAPIView):
    serializer_class = EnumSerializer


class EnumListAPIView(ListAPIView):
    serializer_class = EnumSerializer
    queryset = Enum.objects.all()


class EnumDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EnumSerializer
    queryset = Enum.objects.all()
