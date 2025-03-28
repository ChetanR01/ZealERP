from django.shortcuts import render, redirect, get_object_or_404,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import ExtendedUser

from studentApp.models import Course
from facultyApp.models import notification

from studentApp.models import Course,Student,Division
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404

from adminApp.models import Subject
from .forms import SubjectForm
from studentApp.models import Student,Division
from django.contrib.auth.models import User
from django.contrib import messages
from facultyApp.models import Staff

# Create your views here.
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


# SUBJECT MANAGEMENT
def subject(request):
    subjects = Subject.objects.all()
    return render(request, 'adminApp/manage_subject.html', {'subjects': subjects})

def add_subject(request) :
    if request.method == "POST":
        form =SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/manage-subject")
        data = Subject.objects.all()
    else:
        form =SubjectForm()
        data = Subject.objects.all()
    return render(request, 'adminApp/add_subject.html', {'data':data, 'form' : form})

def update_subject(request, id):
    if request.method == "POST":
        pi = Subject.objects.get(pk=id)
        fm = SubjectForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect("/manage-subject")
    else :
        pi= Subject.objects.get(pk=id)
        fm =SubjectForm(instance=pi)
    return render(request, 'adminApp/update_subject.html', {'form':fm})
    
def delete_subject(request, id):
    pi = get_object_or_404(Subject, pk=id)  # Handle case where subject doesn't exist
    print("subj id", pi)
    if request.method == "POST":
        pi.delete()
        print("deleted")
        return HttpResponseRedirect("/manage-subject")
    
    # If a GET request is made, redirect or show a confirmation page
    return redirect("/manage-subject") 




# COURSE MANAGEMENT
def courses(request):
    courses = Course.objects.all()
    return render(request, 'adminApp/manage_course.html', {'courses': courses})

def create_notification(request):
    if request.method == "POST":
        name = request.POST["name"]
        title = request.POST["title"]
        desc = request.POST["desc"]
        notif_type = request.POST["type"]
        url = request.POST['url']
        notification.objects.create(sender_name=name, title=title, detail_des=desc,  notification_type=notif_type, url=url)
        return render(request, "adminApp/notification.html")
    else:
        return render(request, "adminApp/notification.html")
    
def show_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"adminApp/notificate.html",{'data':notifications})

def show_notifications(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"studentApp/notifications.html",{'data':notifications})

def show_fac_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    return render(request,"facultyApp/notification.html",{'data':notifications})

def del_notificate(request):
    data = notification.objects.all().order_by('-created_at')
    return render(request,'adminApp/delete_notification.html',{'noti':data})

def del_notification(request, id):
    notify = get_object_or_404(notification, id=id)
    notify.delete()
    return redirect('/delete_notificate')

def divisions(request):
    divisions = Division.objects.all()
    return render(request, 'adminApp/manage_division.html',{'divisions':divisions})

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


def add_division(request):
    if request.method == "POST":
        name = request.POST.get("name")

        academic_year = request.POST.get("academic")
        course_id = request.POST.get("course_id")  # Fetch the selected course ID

        if not course_id:
            return render(request, "adminApp/add_division.html", {
                "error": "Please select a course.",
                "courses": Course.objects.all()
            })

        course = Course.objects.get(id=course_id)  # Get the course object

        Division.objects.create(name=name, academic_year=academic_year, course=course)

        return redirect("/manage-division")  # Redirect after successful addition

    data = Course.objects.all()
    return render(request, "adminApp/add_division.html", {"courses": data})

def edit_division(request, division_id):
    try:
        division = Division.objects.get(id=division_id)
    except Division.DoesNotExist:
        return HttpResponse("Division not found", status=404)

    if request.method == 'POST':
        division_name = request.POST.get('name')
        division_academic = request.POST.get('academic_year')

        division.name = division_name
        division.academic_year = division_academic  
        division.save()

        return redirect('/manage-division')  # Corrected redirect

    return render(request, 'adminApp/edit_division.html', {'division': division})


def delete_division(request, division_id):
    try:
        division = Division.objects.get(id=division_id)
        division.delete()
        return redirect('/manage-division')  # Corrected redirect
    except Division.DoesNotExist:
        return HttpResponse("Division not found", status=404)



def manage_student(request):
    Courses = Course.objects.all()
    divisions = Division.objects.all()
    students = Student.objects.all()
    return render(request,'adminApp/manage_student.html', locals()) 



def add_student(request):
    Courses = Course.objects.all()
    divisions = Division.objects.all()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
       
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']
        enrollment_number = request.POST['enrollment_number']
        #course_id = request.POST['course']
        #division_id = request.POST['division']
        course_id = request.POST['course']
        division_id = request.POST['division']

        course = Course.objects.get(id=course_id)
        division = Division.objects.get(id=division_id)
        

        if Student.objects.filter(enrollment_number=enrollment_number).exists():
            messages.error(request, "Enrollment number already exists.")
            return redirect('add_student')
        username = email

        user = User.objects.create_user(
            username=username, email=email, password=password,
            first_name=first_name, last_name=last_name,
           
        )

        extended_user = ExtendedUser.objects.create(user=user, user_type='student')

        student = Student(
            user=user,
            enrollment_number=enrollment_number,
            dob=dob,
            gender=gender,
            course=course,
            division=division,
            
        )
        student.save()

        messages.success(request, "Student added successfully.")
        return redirect('manage_student')
    return render(request, 'adminApp/add_student.html', locals()) 

   
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
    return render(request, 'adminApp/update_student.html', locals())

#manage staff
def manage_staff(request):
    staff_members = Staff.objects.all()
    return render(request, 'adminApp/manage_staff.html', {'staff_members': staff_members})

def add_staff(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        designation = request.POST['designation']
        joining_date = request.POST['joining_date']
        is_gfm = request.POST.get('is_gfm', False)
        password = request.POST['password']

        if Staff.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('add_staff')
        
        user = User.objects.create_user(
            username=email, email=email, password=password,
            first_name=first_name, last_name=last_name
        )
         
        ExtendedUser.objects.create(user=user, user_type = "staff")

        staff = Staff.objects.create(
            user=user,
            email=email,
            phone=phone,
            designation=designation,
            joining_date=joining_date,
            is_gfm=bool(is_gfm)
        )
        staff.save()

        messages.success(request, "Staff member added successfully!")
        return redirect('manage_staff')
    
    return render(request, 'adminApp/add_staff.html')

def update_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if (request.method == 'POST'):
        staff.user.first_name = request.POST['first_name']
        staff.user.last_name = request.POST['last_name']
        staff.email = request.POST['email']
        staff.phone = request.POST['phone']
        staff.designation = request.POST['designation']
        staff.joining_date = request.POST['joining_date']
        staff.is_gfm = request.POST.get('is_gfm', False)

        staff.user.save()
        staff.save()

        messages.success(request, "Staff details updated successfully!")
        return redirect('manage_staff')
    
    return render(request, 'adminApp/update_staff.html', {'staff': staff})

def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        user = staff.user
        staff.delete()
        user.delete()

        messages.success(request, "Staff details updated successfully!")
        return redirect('manage_staff')
    return render(request, 'adminApp/delete_staff.html',{'staff':staff})

