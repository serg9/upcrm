from django.urls import path

from .views import EnumListAPIView, EnumDetailView, EnumCreateAPIView

urlpatterns = [
    path('enum/create/', EnumCreateAPIView.as_view()),
    path('enum/all/', EnumListAPIView.as_view()),
    path('enum/detail/<int:pk>/', EnumDetailView.as_view()),
]
