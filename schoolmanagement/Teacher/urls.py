from django.urls import path, include

from Teacher import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main1/', views.main1, name='main1'),
    path('register1/', views.register1, name='register1'),
    path('login/', views.login, name='login'),
    path('logout2/', views.logout2, name='logout2'),
    path('about1/', views.about1, name='about1'),
    path('view/', views.view, name='view'),
    path('add/<user_id>', views.add, name='add'),
    path('results/', views.results, name='results'),
    path('attendance/', views.attendance, name='attendance'),
    path('add_attendance/<user_id>', views.add_attendance, name='add_attendance'),
    path('search/', views.search, name='search'),

]
