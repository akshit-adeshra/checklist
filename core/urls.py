from django.urls import path
from core.views import TestAPIView, CheckListsAPIView, CheckListAPIView


urlpatterns = [
    path('', TestAPIView.as_view()),
    path('api/checklists/', CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/', CheckListAPIView.as_view()),
]
