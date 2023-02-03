from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from student.models import User, mark_list, Attendance, subject

from django.db.models import Q


@cache_control(no_cache=True, must_revalidate=True)
def main1(request):
    try:
        box = request.session['email']
        if box is not None:
            return render(request, 'main1.html')
    except:
        messages.info(request, 'Please login')
        return redirect('login')


def about1(request):
    try:
        box = request.session['email']
        if box is not None:
            return render(request, 'about.html')
    except:
        messages.info(request, 'Please login')
        return redirect('login')


@cache_control(no_cache=True, must_revalidate=True)
def home(request):
    try:
        box = request.session['email']
        if box is not None:
            return render(request, 'home.html')
    except:
        # messages.info(request, 'Please login')
        return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).exists()
        print(user)

        if user is True:
            a = User.objects.filter(email=email)
            print(a, '====================================================================')
            for i in a:
                if i.roll == "Teacher":
                    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    request.session['email'] = email
                    request.session['standard'] = i.standard
                    print(email)
                    return redirect('main1')
                else:
                    messages.info(request, 'invalid email id Or password')
                    return redirect('login')
        else:
            messages.info(request, 'user does not exists')
            return redirect('login')
    return render(request, 't_login.html')


def register1(request):
    sub = subject.objects.all()
    print(sub,
          '::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        gender = request.POST['gender']
        dob = request.POST['dob']
        mobile_no = request.POST['mobile_no']
        date_joined = request.POST['date_joined']
        roll = request.POST['roll']
        standard = request.POST['standard']
        Subject = subject.objects.get(id=request.POST['name'])
        image = request.FILES['image']

        if roll == "Teacher":
            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password,
                                address=address, gender=gender, dob=dob, mobile_no=mobile_no, date_joined=date_joined,
                                roll=roll, image=image, standard=standard, Subject=Subject)
            return redirect('login')
        else:
            User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password,
                                address=address, gender=gender, dob=dob, mobile_no=mobile_no, date_joined=date_joined,
                                roll=roll, image=image, standard=standard, Subject=Subject)
            return redirect('adminlogin')
    return render(request, 't_register.html', {'key': sub})


def logout2(request):
    try:
        box = request.session['email']
        if box is not None:
            del request.session['email']
            logout(request)
            return redirect('home')
    except:
        messages.info(request, 'Please login')
        return redirect('login')


def view(request):
    try:
        box = request.session['email']
        if box is not None:
            a = User.objects.filter(roll='Student')
            print(a)
            # for i in a:
            #     if i.roll == 'Student':
            #         print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

            return render(request, 'view.html', {'key': a})
    except:

        return redirect('home')


def add(request, user_id):
    sub = subject.objects.all()
    print(sub, '####################')
    list1 = []
    for i in sub:
        subjects = i.name
        print(subjects, '@@@@@@@@@@@@@@@')
        list1.append(subjects)
    print(list1)
    data = mark_list.objects.filter(user_id=user_id).exists()
    print(data)

    a = User.objects.filter(id=user_id)
    print(a, '000000000000000000000000000000000')
    for i in a:
        print(i.first_name)
        user = i.first_name
        print(user, '++++++++++++++++++++++++++++++++++')
    if request.method == "POST":
        s1 = request.POST.get('s1')
        s2 = request.POST.get('s2')
        s3 = request.POST.get('s3')
        s4 = request.POST.get('s4')
        s5 = request.POST.get('s5')
        print(type(s1), '=============================================')
        total = int(s1) + int(s2) + int(s3) + int(s4) + int(s5)
        print(total, '/////////////////////////////////////////////////////////////////////////////////////')
        percentage = total * 100 / 500;
        print(percentage, '?????????????????????????????????????????????????????????????///////?????????????')
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B+"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = 'failed'
        if data is False:
            list1 = mark_list.objects.create(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, total=total, percentage=percentage,
                                             grade=grade, user=user, user_id=user_id)
            list1.save()
            return redirect('results')
        else:
            up = mark_list.objects.filter(user_id=user_id).update(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, total=total,
                                                                  percentage=percentage, grade=grade, user=user,
                                                                  user_id=user_id)
            return redirect('results')
    return render(request, 'add.html', {'key': list1})


def results(request):
    try:
        box = request.session['email']
        if box is not None:
            result = mark_list.objects.all()
            print(result, '+++++++++++++++++++++++++++++++++++++++++++++')
            return render(request, 'results.html', {'key': result})
    except:
        messages.info(request, 'Please login')
        return redirect('login')


def attendance(request):
    try:
        box = request.session['email']
        if box is not None:
            data = request.session['email']
            print(data, '{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}')
            standard = request.session['standard']
            print(standard, "++++++++++++++++++++++++++++++++")

            std = User.objects.filter(email=data, is_tutor=True)
            print(len(std))
            if len(std) == 1:
                print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
                a = User.objects.filter(standard=standard, roll='Student')
                print(a, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                for i in a:
                    print(i.first_name)
                return render(request, 'attendance.html', {'key': a})
            else:
                messages.info(request, 'you are Not a Tutor')
                return redirect('main1')
    except:
        messages.info(request, 'Please login')
        return redirect('login')
    # return render(request, 'attendance.html')


def add_attendance(request, user_id):
    data = User.objects.filter(id=user_id)
    print(data, '{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}')
    for i in data:
        print(i.first_name)
        print(i.standard)
        student_name = i.first_name
        standard = i.standard
    if request.method == 'POST':
        date = request.POST['date']
        value = request.POST['attendance']
        print(value, '????????????????????????????????????????????')
        print(date, '????????????????????????')
        d = Attendance.objects.filter(user_id=user_id)
        for i in d:
            print(i.student_name)
            f = i.attendance
            da = i.date

        print(d, 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
        if da != date:
            if value == 'True':
                att = 'x'
            else:
                att = 'a'

            a = Attendance.objects.create(student_name=student_name, standard=standard, date=date,
                                          attendance=att, user_id=user_id)
            print(a, '()))))))))))))))))))))))))))))')
        else:
            messages.info(request, 'attendance already added')

    return redirect('main1')


# def search(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         print(searched, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#         a = User.objects.filter(roll='Student')
#         print(a)
#         for i in a:
#             standard = i.standard
#             first_name = i.first_name
#             print(standard)
#             if searched == standard:
#                 print('############################################################')
#                 return render(request, 'view.html', {'key': a})
#             elif searched == first_name:
#                 print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#                 return render(request, 'view.html', {'key': a})
#             else:
#                 messages.info(request, 'match not found')
#     # return render(request, 'view.html')
#     # return render(request, 'view.html', {'key': searched})
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        print(searched, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        if User.objects.filter(standard=searched, roll='Student') or User.objects.filter(first_name=searched,
                                                                                         roll='Student'):
            a = User.objects.filter(Q(standard=searched, roll='Student') | Q(first_name=searched, roll='Student'))
            print('############################################################')
            print(a)
            return render(request, 'view.html', {'key': a})
    # return render(request, 'view.html')
    # return render(request, 'view.html', {'key': searched})
