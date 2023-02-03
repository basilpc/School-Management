from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from student.models import User, mark_list, Attendance


@cache_control(no_cache=True, must_revalidate=True)
def adminmain(request):
    try:
        box = request.session['email']
        if box is not None:
            return render(request, 'adminmain.html')
    except:
        messages.info(request, 'Please login')
        return redirect('adminlogin')


@cache_control(no_cache=True, must_revalidate=True)
def adminhome(request):
    try:
        box = request.session['email']
        if box is not None:
            return render(request, 'adminhome.html')
    except:
        # messages.info(request, 'Please login')
        return render(request, 'adminhome.html')


def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).exists()
        print(user)
        if user is True:
            a = User.objects.filter(email=email)
            print(a)
            for i in a:
                print(i.roll)
                if i.roll == 'Admin':
                    request.session['email'] = email
                    return redirect('adminmain')
            else:
                messages.info(request, 'invalid emailid Or password')
                return redirect('adminlogin')
        else:
            messages.info(request, 'user Does not exists')
            return redirect('adminlogin')

    return render(request, 'adminlogin.html')


def students(request):
    try:
        box = request.session['email']
        if box is not None:
            a = User.objects.filter(roll='Student')
            print(a)
            return render(request, 'students.html', {'key': a})
    except:
        messages.info(request, 'Please login')
        return redirect(adminlogin)


def teachers(request):
    try:
        box = request.session['email']
        if box is not None:
            a = User.objects.filter(roll='Teacher')
            print(a)
            return render(request, 'teachers.html', {'key': a})
    except:
        messages.info(request, 'Please login')
        return redirect(adminlogin)


def delete(request, user_id):
    a = User.objects.filter(id=user_id)
    print(a, '[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]][[[[[[[[[[[[[[[[[')
    a.delete()
    b = mark_list.objects.filter(user_id=user_id)
    print(b, '}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}')
    b.delete()
    return redirect('students')


def remove(request, user_id):
    c = User.objects.filter(id=user_id)
    print(c, '|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    c.delete()
    return redirect('teachers')


def logout3(request):
    try:
        box = request.session['email']
        if box is not None:
            del request.session['email']
            logout(request)
            return redirect('adminhome')
    except:
        messages.info(request, 'Please login')
        return redirect('adminlogin')


def update(request, user_id):
    a = User.objects.get(id=user_id)
    print(a, '###############################################################')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        address = request.POST['address']
        standard = request.POST['standard']

        dob = request.POST['dob']
        admission_number = request.POST['admission_number']
        blood_group = request.POST['blood_group']
        image = request.FILES['image']
        up = User.objects.filter(id=user_id).update(first_name=first_name, address=address, standard=standard,
                                                    dob=dob, admission_number=admission_number,
                                                    blood_group=blood_group, image=image)
        save = User.objects.get(id=user_id)
        save.save()
        return redirect(students)

    return render(request, 'update.html', {'key': a})


def edit(request, user_id):
    a = User.objects.get(id=user_id)
    print(a, '??????????????????????????????????????????????????????????')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        address = request.POST['address']

        dob = request.POST['dob']
        mobile_no = request.POST['mobile_no']
        Teaching_subjects = request.POST['Teaching_subjects']
        image = request.FILES['image']
        up = User.objects.filter(id=user_id).update(first_name=first_name, address=address, dob=dob,
                                                    mobile_no=mobile_no, Teaching_subjects=Teaching_subjects,
                                                    image=image)
        s = User.objects.get(id=user_id)
        s.save()
        return redirect(teachers)
    return render(request, 'edit.html', {'key': a})


def mark(request):
    try:
        box = request.session['email']
        if box is not None:
            a = mark_list.objects.all()
            print(a, '''''''''''''''''''''''''''''''''''')
            return render(request, 'mark.html', {'key': a})
    except:
        messages.info(request, 'Please login')
        return redirect(adminlogin)


def maketutor(request, user_id):
    a = User.objects.get(id=user_id)
    print(a,
          ')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
    if request.method == 'POST':
        print('?????????????????????????????????????????????????????')
        is_tutor = request.POST['is_tutor']
        make = User.objects.filter(id=user_id).update(is_tutor=is_tutor)
        tutor = User.objects.get(id=user_id)
        tutor.save()
        print(tutor)
        return redirect('teachers')


def view_attendence(request):
    try:
        box = request.session['email']
        if box is not None:
            data = Attendance.objects.all()
            print(data)
            return render(request, 'view_attendence.html', {'key': data})
    except:
        messages.info(request, 'Please login')
        return redirect('adminlogin')


def searching(request):
    if request.method == 'POST':
        search = request.POST['search']
        print(search, '{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}')
        a = User.objects.filter(first_name__contains=search, roll='Teacher')

    return render(request, 'teachers.html', {'key': a})
