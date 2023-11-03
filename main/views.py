from django.shortcuts import render,redirect
from django.contrib import messages
from .models import studentModel,teachersModel,courseModel,booksModel

# Create your views here.
def dashboard_view(request):
     student_count = studentModel.objects.count()
     student_ = studentModel.objects.all()
     teachers_count = teachersModel.objects.count()
     teachers_ = teachersModel.objects.all()
     course_count = courseModel.objects.count()
     books_count = booksModel.objects.count()

     context = {
          'student_count': student_count,
          'teachers_count' : teachers_count,
          'course_count' : course_count,
          'books_count' : books_count,
          'student' : student_,
          'teachers' : teachers_

     }
     return render(request, 'dashborad.html' , context)


def student_view(request):
    if request.method == "POST":
        fname = request.POST['first-name']
        lname = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        course = request.POST['course']
        new_student = studentModel.objects.create(
            first_name = fname,
            last_name = lname,
            email= email,
            mobile=mobile,
            course_name_id=course
        )
        new_student.save()
        return redirect('student_view')
    student_ = studentModel.objects.all()
    courses_ = courseModel.objects.all()
    context = {
        'students' : student_,
        'courses':courses_
    }
    return render(request, 'student.html',context)

def updateStudent(request,student_id):
    if request.method == 'POST':
          fname = request.POST['first-name']
          lname = request.POST['last_name']
          email = request.POST['email']
          mobile = request.POST['mobile']
          course = request.POST['course']
          update_student = studentModel.objects.get(id=student_id)
          update_student.first_name = fname
          update_student.last_name = lname
          update_student.email = email
          update_student.mobile = mobile
          update_student.course_name_id = course
          update_student.save()
          return redirect('student_view')
    
    courses_ = courseModel.objects.all()
    update_student = studentModel.objects.get(id=student_id)
    context = {
        'first-name':update_student.first_name,
        'last_name': update_student.last_name,
        'email': update_student.email,
        'mobile': update_student.mobile,
        'course_name': update_student.course_name_id,
        'courses':courses_

    }
    return render (request,'update_student.html',context)

     
# def addStudent(request):
#     if request.method == 'POST':
#         full_name = request.POST["full_name"]
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         mobile = request.POST['mobile']
#         course = request.POST['course']

#         student_id = request.session.get

#         create_student = studentModel.objects.create(
#             full_name = full_name,
#             last_name=last_name,
#             email=email,
#             mobile=mobile,
#             course=course
#         )
#         create_student.save()
#         messages.success(request, f'{full_name} - student added')
#         return redirect('student_view')
#     return redirect('student_view')

def teachers_view(request):
     teachers_ = teachersModel.objects.all()
     context = {
          'teachers' : teachers_
          }
     return render(request, 'teachers.html',context)

def course_view(request):
    course = courseModel.objects.all()
    context = {
        'courses' : course
    }
    return render(request,'course.html',context)

def books_view(request):
    books_ = booksModel.objects.all()
    context = {
        'books' : books_
     }
    return render(request,'books.html',context)

def profile_view(request):
     return render(request, 'profile.html')

