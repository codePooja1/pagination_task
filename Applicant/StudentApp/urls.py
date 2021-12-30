from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.addStudentView,name='add_student'),
    path('show/',views.showStudentView,name='show_student'),
    path('update/<int:i>/',views.updateStudentView,name='update'),
    path('delete/<int:i>/',views.deleteStudentView,name='delete'),
]