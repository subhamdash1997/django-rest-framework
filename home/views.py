from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'message':'something went wrong.'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        # token_obj,_=Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({'status':201,'payload':serializer.data,'refresh':str(refresh),'access':str(refresh.access_token),'message':'saved successfully.'})


class StudentAPI(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    
    def post(self,request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if not serializer.is_valid():
            return Response({'status':403,'message':'something went wrong.'})
        serializer.save()
        return Response({'status':201,'payload':serializer.data,'message':'saved successfully.'})
        
    def put(self,request):
        pass

    def patch(self,request):
        try:
            student_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(student_obj,data=request.data,partial = True)
            if not serializer.is_valid():
                return Response({'status':403,'message':'something went wrong.'})
            serializer.save()
            return Response({'status':201,'payload':serializer.data,'message':'saved successfully.'})
        except Exception as e:
            return Response({'status':500,'message':'internal server error.'})

    def delete(self,request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status':201,'message':'deleted successfully.'})
        except Exception as e:
            return Response({'status':500,'message':'internal server error.'})


















# @api_view(['GET'])
# def get_categories(request):
#     categories = Category.objects.all()
#     serializer = CategorySerializer(categories,many=True)
#     return Response({'status':200,'payload':serializer.data})

# @api_view(['GET'])
# def get_books(request):
#     book_objs = Book.objects.all()
#     serializer = BookSerializer(book_objs,many=True)
#     return Response({'status':200,'payload':serializer.data})

# # Create your views here.
# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs,many=True)
#     return Response({'status':200,'payload':serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=data)
#     if not serializer.is_valid():
#         return Response({'status':403,'message':'something went wrong.'})
#     serializer.save()
#     return Response({'status':201,'payload':serializer.data,'message':'saved successfully.'})

# @api_view(['PATCH'])
# def update_student(request,id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj,data=request.data,partial = True)
#         if not serializer.is_valid():
#             return Response({'status':403,'message':'something went wrong.'})
#         serializer.save()
#         return Response({'status':201,'payload':serializer.data,'message':'saved successfully.'})
#     except Exception as e:
#         return Response({'status':500,'message':'internal server error.'})

# @api_view(['DELETE'])
# def delete_student(request):
#     try:
#         id = request.GET.get('id')
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':201,'message':'deleted successfully.'})
#     except Exception as e:
#         return Response({'status':500,'message':'internal server error.'})
    
    