from django.urls import path
from core.views import TestAPIView, CheckListsAPIView, CheckListAPIView, CheckListItemCreateAPIView, CheckListItemAPIView


urlpatterns = [
    path('', TestAPIView.as_view()),
    path('api/checklists/', CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/', CheckListAPIView.as_view()),
    path('api/checklistItem/create/', CheckListItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>/', CheckListItemAPIView.as_view()),
]
