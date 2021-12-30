from django.shortcuts import render,redirect
from .forms import StudentModelForm
from .models import Student
from django.core.paginator import Paginator

def addStudentView(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_student")
    template_name = 'StudentApp/addStudent.html'
    context = {'form':form}
    return render(request, template_name, context)

def showStudentView(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'StudentApp/showStudent.html'
    context = {'page_obj':page_obj}
    return render(request, template_name, context)

def updateStudentView(request,i):
    student = Student.objects.get(id=i)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("show_student")
    template_name = 'StudentApp/addStudent.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteStudentView(request,i):
    student = Student.objects.get(id=i)
    student.delete()
    return redirect("show_student")