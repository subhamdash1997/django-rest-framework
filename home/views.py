from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if not serializer.is_valid():
        return Response({'status':403,'message':'something went wrong.'})
    serializer.save()
    return Response({'status':201,'payload':serializer.data,'message':'saved successfully.'})

@api_view(['PATCH'])
def update_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj,data=request.data,partial = True)
        if not serializer.is_valid():
            return Response({'status':403,'message':'something went wrong.'})
        serializer.save()
        return Response({'status':201,'payload':serializer.data,'message':'saved successfully.'})
    except Exception as e:
        return Response({'status':500,'message':'internal server error.'})

@api_view(['DELETE'])
def delete_student(request):
    try:
        id = request.GET.get('id')
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':201,'message':'deleted successfully.'})
    except Exception as e:
        return Response({'status':500,'message':'internal server error.'})
    
    