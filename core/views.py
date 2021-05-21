from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from core.permissions import IsOwner
from core.models import CheckList, CheckListItem
from core.serializers import CheckListSerializer, CheckListItemSerializer


class CheckListsAPIView(ListCreateAPIView):
    """
    Listing, Creation
    """
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset


class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy
    """
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset


class CheckListItemCreateAPIView(CreateAPIView):
    """
    Creation
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset
