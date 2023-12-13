from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status  # Add this import
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt



class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        output = [{"employee": output.employee, "department": output.department}
                  for output in React.objects.all()]
        return Response(output)
    @csrf_exempt
    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

    def patch(self, request, pk):
        try:
            item = React.objects.get(pk=pk)
        except React.DoesNotExist:
            raise Http404

        serializer = ReactSerializer(item, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
