from django.contrib import messages, auth
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from student.models import User, mark_list, Attendance
from django.views.decorators.cache import cache_control


from reportlab.pdfgen import canvas
from django.http import HttpResponse


@cache_control(no_cache=True, must_revalidate=True)
def main(request):
    try:
        box = request.session['email']
        print('0000000000')
        print(box, "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}")
        if box is not None:
            return render(request, 'main.html')
    except:
        print('exeppppppppppppppppppppppppppppppppppppp')
        # messages.info(request, 'Please Login')
        return redirect('index')


@cache_control(no_cache=True, must_revalidate=True)
def index(request):
    print('99999999999999999999999999999999')

    try:
        box = request.session['email']
        print('0000000000')
        print(box, "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}")
        if box is not None:
            print('indexxxxxxxxxxxxxxxxxxxxxxxx')
            return render(request, 'index.html')
    except:
        print('444444444444444444444444')
        # messages.info(request, 'Please Login')
        return render(request, 'index.html')


@cache_control(no_cache=True, must_revalidate=True)
def sign(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).exists()
        print(user)

        if user is True:
            a = User.objects.filter(email=email)
            print(a, '====================================================================')
            for i in a:
                if i.roll == "Student":
                    print('---------------------------------------------------------')
                    request.session['email'] = email
                    print(email)
                    return redirect('main')
                else:
                    messages.info(request, 'invalid email id Or password')
                    return redirect('login')
        else:
            messages.info(request, 'user does not exists')
            return redirect('sign')
    return render(request, 'contact.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        admission_number = request.POST['admission_number']
        standard = request.POST['standard']
        roll = request.POST['roll']
        image = request.FILES['image']
        blood_group = request.POST['blood_group']
        gender = request.POST['gender']
        User.objects.create(first_name=first_name, last_name=last_name, address=address, email=email,
                            password=password, dob=dob, admission_number=admission_number,
                            standard=standard, roll=roll, image=image, blood_group=blood_group,
                            gender=gender)

        return redirect('sign')

    return render(request, 's_registration.html')


def s_details(request):
    try:
        box = request.session['email']
        if box is not None:
            email = request.session['email']
            print(email)
            a = User.objects.filter(email=email)
            for i in a:
                print(i.admission_number)

            return render(request, 's_details.html', {'key': a})
    except:
        messages.info(request, 'Please Login')
        return redirect('sign')


def logout1(request):
    try:
        box = request.session['email']
        if box is not None:
            print('logoutttttttttttttttttttttttttttttttt')
            del request.session['email']
            logout(request)
            return redirect('index')
    except:
        messages.info(request, 'Please login')
        return redirect('sign')


def about(request):
    try:
        box = request.session['email']
        if box is not None:
            return render(request, 'about.html')
    except:
        messages.info(request, 'Please login')
        return redirect('sign')


def result(request):
    try:
        box = request.session['email']
        if box is not None:
            email = request.session['email']
            print(email)
            a = User.objects.filter(email=email)
            for i in a:
                print(i.first_name)
                user = i.first_name
                print(user, '#######################################################')
            mark = mark_list.objects.filter(user=user)
            print(mark, '_________________________________________________________')
            for i in mark:
                print(i.user)
                print(i.grade)
                print(i.total)
                print(i.percentage)
            return render(request, 'result.html', {'key': mark})
    except:
        messages.info(request, 'Please login')
        return redirect('sign')


def download(request):
    email = request.session['email']
    print(email)
    a = User.objects.filter(email=email)
    for i in a:
        print(i.first_name)
        user = i.first_name
        print(user, '#######################################################')
    mark = mark_list.objects.filter(user=user)
    print(mark, '_________________________________________________________')
    name = None
    grade = None
    for i in mark:
        name = i.user
        Chemistry = i.s1
        Physics = i.s2
        English = i.s3
        Maths = i.s4
        History = i.s5
        Total = i.total
        Percentage = i.percentage
        grade = i.grade

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)

    p.setFont('Helvetica', 12)
    p.drawString(260, 700, "MARK LIST")

    p.drawString(175, 600, 'NAME')
    p.drawString(350, 600, name)

    p.drawString(175, 575, 'Chemistry')
    p.drawString(350, 575, str(Chemistry))

    p.drawString(175, 550, 'Physics')
    p.drawString(350, 550, str(Physics))

    p.drawString(175, 525, 'English')
    p.drawString(350, 525, str(English))

    p.drawString(175, 500, 'Maths')
    p.drawString(350, 500, str(Maths))

    p.drawString(175, 475, 'History')
    p.drawString(350, 475, str(History))

    p.drawString(175, 450, 'Total')
    p.drawString(350, 450, str(Total))

    p.drawString(175, 425, 'Percentage')
    p.drawString(350, 425, str(Percentage))

    p.drawString(175, 405, 'grade')
    p.drawString(350, 405, str(grade))

    p.showPage()
    p.save()
    return response


def s_a_v(request):
    email = request.session['email']
    print(email)
    a = User.objects.filter(email=email)
    for i in a:
        print(i.first_name)
        user = i.first_name
        print(user, '#######################################################')
    att = Attendance.objects.filter(student_name=user)
    print(att, '_________________________________________________________')
    for i in att:
        print(i.user_id)
        name = i.student_name
        standard = i.standard
        print(name)
        print(standard)
    return render(request, 's_a_v.html', {'key': att, 'name': name, 'standard': standard}, )
