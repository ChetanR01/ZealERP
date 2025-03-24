from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('', views.dashboard, name='dashboard'),
    path('manage-course', views.courses, name='courses'),
    path('notification', views.create_notification, name='notification'),
    path('notify', views.show_notification, name='notify'),
    path('delete_notificate', views.del_notificate, name='delete_notificate'),
    path('delete_notification/<int:id>', views.del_notification, name='del_notification'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)