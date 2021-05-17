from django.http.response import Http404
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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

        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer

    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)

        # just as in saving form data, we need to associate this data with a particular instance of the model,
        # so model is also passed as the first argument
        serializer = self.serializer_class(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
