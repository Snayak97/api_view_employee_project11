from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def EmployeeData(request):
    EMPDATA=Employee.objects.all()
    EMPJSONDATA=EmployeeMS(EMPDATA,many=True)
    return Response(EMPJSONDATA.data)