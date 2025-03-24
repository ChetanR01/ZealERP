from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import ExtendedUser
from studentApp.models import Course
from facultyApp.models import notification
from django.shortcuts import get_object_or_404


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
        # Save to the database
        notification.objects.create(sender_name=name, title=title, detail_des=desc,  notification_type=notif_type, url=url)
        return render(request, "adminApp/notification.html")
    else:
        return render(request, "adminApp/notification.html")
    
def show_notification(request):
    notifications = notification.objects.all().order_by('-created_at')
    for noti in notifications:
        print(noti)
    return render(request,"adminApp/notificate.html",{'data':notifications})

def del_notificate(request):
    data = notification.objects.all().order_by('-created_at')
    return render(request,'adminApp/delete_notification.html',{'noti':data})

def del_notification(request, id):
    notify = get_object_or_404(notification, id=id)
    notify.delete()
    return redirect('/delete_notificate')
