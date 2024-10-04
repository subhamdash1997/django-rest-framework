from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home),
    path('student/',post_student),
    path('update-student/<id>/',update_student),
    path('delete-student/',delete_student)
]