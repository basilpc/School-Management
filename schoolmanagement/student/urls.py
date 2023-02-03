from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from student import views

urlpatterns = [

    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('sign/', views.sign, name='sign'),
    path('register/', views.register, name='register'),
    path('s_details/', views.s_details, name='s_details'),
    path('logout1/', views.logout1, name='logout1'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
    path('download/', views.download, name='download'),
    path('s_a_v/', views.s_a_v, name='s_a_v'),
]
