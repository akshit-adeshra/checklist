from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import CheckList
from core.serializers import CheckListSerializer


class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({'name': 'Akshit from CBV'})


class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer

    def get(self, request, format=None):
        data = CheckList.objects.all()

        # instantiating the serializer class, & giving it the queryset data as parameter
        serializer = self.serializer_class(data, many=True)

        # fetching the serialized data from the serializer
        serialized_data = serializer.data

        return Response(serialized_data)
