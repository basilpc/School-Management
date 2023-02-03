from django.urls import path

from owner import views

urlpatterns = [
    path('', views.adminhome, name='adminhome'),
    path('adminmain/', views.adminmain, name='adminmain'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('delete/<user_id>', views.delete, name='delete'),
    path('remove/<user_id>', views.remove, name='remove'),
    path('logout3/', views.logout3, name='logout3'),
    path('update/<user_id>', views.update, name='update'),
    path('edit/<user_id>', views.edit, name='edit'),
    path('mark/', views.mark, name='mark'),
    path('maketutor/<user_id>', views.maketutor, name='maketutor'),
    path('view_attendence/', views.view_attendence, name='view_attendence'),
    path('searching/', views.searching, name='searching'),
]
