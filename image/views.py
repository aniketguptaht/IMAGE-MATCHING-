import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ImageSerializer
from .models import Pictures
from rest_framework.response import Response
import json
# Create your views here.

class DisplayView(APIView):
   queryset = Pictures.objects.all()
   serializer_class = ImageSerializer

   def post(self, request, *args, **kwargs):
      file = ''
      try:
         file = request.POST.get('file')
      except KeyError:
         return Response(json.dumps({'message': "Not Uploaded"}), status=400)   
      name = request.POST.get('name')
      if file:
         return Response(json.dumps({'message': "Uploaded"}), status=200)   
      return Response(json.dumps({'message': "No file found"}), status=400)   

        
        