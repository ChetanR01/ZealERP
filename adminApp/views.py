from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import ExtendedUser
from studentApp.models import Course,Student,Division
from django.contrib.auth.models import User
from django.contrib import messages

def signin(request):
    if request.method == "POST":
        user_type = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate( request,username=email, password=password)
        if user is not None:
            ex_user = ExtendedUser.objects.get(user=user.id)
            if ex_user.user_type == user_type:
                print("User Type Correct!")
                # redirect to corresponding dashboard
                if user_type == "admin":
                    login(request, user)
                    return redirect('/')
                elif user_type == "student":
                    login(request, user)
                    return redirect('/student')
                elif user_type == "staff":
                    login(request, user)
                    return redirect('/staff')
        else:
            print("Invalid Credentials!!")
            return redirect('/signin')
        
    return render(request, 'signin.html')



def dashboard(request):
    return render(request, 'adminApp/index.html')


def courses(request):
    courses = Course.objects.all()
    return render(request, 'adminApp/manage_course.html', {'courses': courses})

def edit_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponse("Course not found", status=404)

    if request.method == 'POST':
        course_name = request.POST.get('name')
        course_duration = request.POST.get('duration')
        course_is_active = request.POST.get('is_active') == 'True'

        course.name = course_name
        course.duration = course_duration
        course.is_active = course_is_active
        course.save()

        return redirect('manage_course')  # Corrected redirect

    return render(request, 'adminApp/edit_course.html', {'course': course})

def delete_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
        return redirect('manage_course')  # Corrected redirect
    except Course.DoesNotExist:
        return HttpResponse("Course not found", status=404)

def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('name')
        course_duration = request.POST.get('duration')
        course_is_active = request.POST.get('is_active') == 'True'

        Course.objects.create(
            name=course_name,
            duration=course_duration,
            is_active=course_is_active
        )
        return redirect('manage_course') #redirect after adding a course

    return render(request, 'adminApp/add_course.html')



def manage_student(request):
    Courses = Course.objects.all()
    divisions = Division.objects.all()
    students = Student.objects.all()
    return render(request,'adminApp/manage_student.html', locals()) 

from django.db import transaction

def add_student(request):
    Courses = Course.objects.all()
    divisions = Division.objects.all()
    
    if request.method == "POST":
        try:
            # Get form data with safe defaults
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            email = request.POST.get('email', '').strip()
            password = request.POST.get('password', '').strip()
            dob = request.POST.get('dob', '').strip()
            gender = request.POST.get('gender', '').strip()
            enrollment_number = request.POST.get('enrollment_number', '').strip()
            phone = request.POST.get('phone', '').strip()
            course_id = request.POST.get('course', '').strip()
            division_id = request.POST.get('division', '').strip()
            guardian_name = request.POST.get('guardian_name', '').strip()
            guardian_phone = request.POST.get('guardian_phone', '').strip()

            # Validate required fields
            required_fields = {
                'First Name': first_name,
                'Last Name': last_name,
                'Email': email,
                'Password': password,
                'Date of Birth': dob,
                'Gender': gender,
                'Enrollment Number': enrollment_number,
                'Phone': phone,
                'Course': course_id,
                'Division': division_id
            }
            
            for field, value in required_fields.items():
                if not value:
                    messages.error(request, f"{field} is required.")
                    return redirect('add_student')

            # Check for existing user
            if User.objects.filter(username=email).exists():
                messages.error(request, "This email is already registered.")
                return redirect('add_student')

            # Check for existing student records
            if Student.objects.filter(enrollment_number=enrollment_number).exists():
                messages.error(request, "Enrollment number already exists.")
                return redirect('add_student')
            
            if Student.objects.filter(phone=phone).exists():
                messages.error(request, "Phone number already exists.")
                return redirect('add_student')

            # Get related objects
            try:
                course = Course.objects.get(id=course_id)
                division = Division.objects.get(id=division_id)
            except (Course.DoesNotExist, Division.DoesNotExist):
                messages.error(request, "Invalid course or division selected.")
                return redirect('add_student')

            # Create user and student in a transaction
            with transaction.atomic():
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                student = Student(
                    user=user,
                    enrollment_number=enrollment_number,
                    dob=dob,
                    gender=gender,
                    phone=phone,
                    course=course,
                    division=division,
                    guardian_name=guardian_name,
                    guardian_phone=guardian_phone
                )
                student.save()

            messages.success(request, "Student added successfully.")
            return redirect('manage_student')

        except Exception as e:
            messages.error(request, f"Error adding student: {str(e)}")
            return redirect('add_student')

    return render(request, 'adminApp/add_student.html', {'Courses': Courses, 'divisions': divisions})

   
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        user = student.user 

        student.delete() 
        user.delete() 

        messages.success(request, "Student deleted successfully.")
        return redirect('manage_student')
    
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    courses = Course.objects.all()
    divisions = Division.objects.all()

    if request.method == "POST":
        # Update only fields that are present in request.POST and are not empty
        if 'first_name' in request.POST and request.POST['first_name']:
            student.user.first_name = request.POST['first_name']
        if 'last_name' in request.POST and request.POST['last_name']:
            student.user.last_name = request.POST['last_name']
        if 'email' in request.POST and request.POST['email']:
            student.user.email = request.POST['email']
        if 'dob' in request.POST and request.POST['dob']:
            student.dob = request.POST['dob']
        if 'gender' in request.POST and request.POST['gender']:
            student.gender = request.POST['gender']
        if 'enrollment_number' in request.POST and request.POST['enrollment_number']:
            if Student.objects.filter(enrollment_number=request.POST['enrollment_number']).exclude(id=student_id).exists():
                messages.error(request, "Enrollment number already exists.")
                return redirect('update_student', student_id=student.id)
            student.enrollment_number = request.POST['enrollment_number']
        if 'course' in request.POST and request.POST['course']:
            student.course = Course.objects.get(id=request.POST['course'])
        if 'division' in request.POST and request.POST['division']:
            student.division = Division.objects.get(id=request.POST['division'])

        student.user.save()  # Save User model changes
        student.save()  # Save Student model changes

        messages.success(request, "Student details updated successfully.")
        return redirect('manage_student')

    return render(request, 'adminApp/update_student.html', locals())