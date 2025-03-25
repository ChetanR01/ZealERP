from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('', views.dashboard, name='dashboard'),


    path('index', views.dashboard, name='dashboard'),

   
    path('manage-subject', views.subject, name='subject'),
    
    
    path('add_subject', views.add_subject , name="add_subject"),
    path("update_subject/<int:id>",views.update_subject, name="update_subject"),
    path("delete_subject/<int:id>",views.delete_subject, name="delete_subject"),
    

  

    path('manage-division', views.divisions, name='divisions'),
    path('add_division', views.add_division, name='divisions'),
    path('edit-division/<int:division_id>/', views.edit_division, name='edit_division'),
    path('delete-division/<int:division_id>/', views.delete_division, name='delete_division'),


    path('manage-course', views.courses, name='manage_course'),
    path('edit-course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),

    path('add-course/', views.add_course, name='add_course'),

  
     path('manage-student',views.manage_student,name ='manage_student'),
    path('add-student',views.add_student,name ='add_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),

    path('manage-staff/', views.manage_staff, name='manage_staff'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('update_staff/<int:staff_id>/', views.update_staff, name='update_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)