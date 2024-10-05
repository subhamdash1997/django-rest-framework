from django.urls import path,include
from .views import *

urlpatterns = [
    path('students/',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view())
    # path('',home),
    # path('student/',post_student),
    # path('update-student/<id>/',update_student),
    # path('delete-student/',delete_student),
    # path('get-books/',get_books),
    # path('get-categories/',get_categories)
]