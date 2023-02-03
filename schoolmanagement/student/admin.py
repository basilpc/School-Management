from django.contrib import admin

# Register your models here.
from student.models import User, mark_list, Attendance, subject

admin.site.register(User)

admin.site.register(mark_list)

admin.site.register(Attendance)

admin.site.register(subject)
