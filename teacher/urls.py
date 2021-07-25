from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.teacher, name='teacher_list'),
    path('teacher_detail/<int:teacher_id>', views.teacher_detail, name="teacher_detail")
]
