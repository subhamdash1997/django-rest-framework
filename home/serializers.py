from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'Age cannot be less than 18.'})

        if data['name']:
            for char in data['name']:
                if char.isdigit():
                    raise serializers.ValidationError({'error': 'Name cannot contain numbers.'})

        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Book
        fields = '__all__'
        
    