from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serilizers import *

# Create your views here.


@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serilizer = StudentSerilizer(student_objs,many=True)
    print(serilizer)
    return Response({'status':200,'payload': serilizer.data})

@api_view(['POST'])
def post_students(request):
    data = request.data
    serilizer = StudentSerilizer(data=request.data)
    if serilizer.is_valid():
        return Response({'status':403,'message':'Something Went Wrong'})
    
    serilizer.save()
    return Response({'status':200,'payload':data,'message':'You sent'})

