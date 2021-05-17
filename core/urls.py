from django.urls import path
from core.views import test_api, TestAPIView


urlpatterns = [
    path('', test_api),
    path('class/', TestAPIView.as_view()),
]
