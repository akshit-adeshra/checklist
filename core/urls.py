from django.urls import path
from core.views import TestAPIView


urlpatterns = [
    path('', TestAPIView.as_view()),
]
