from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET', 'POST'])      # you can specify which methods it'll accept in a list
def test_api(request):
    return Response({'name': 'Akshit'})

class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({'name': 'Akshit from CBV'})
