from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

def teacher(request):
    if request.method == 'POST' and request.FILES['myfile']:
        print('+++++++++++   user wants to upload csv')
        uploaded_file = request.FILES['myfile'].read()
        upload_csv(uploaded_file)
    elif request.method == 'GET' and request.GET.get('lastname'):
        last_name = request.GET.get('lastname')
        teacher = Teacher.objects.filter(last_name__contains=last_name)
    else:
        teacher = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teacher': teacher})


def teacher_detail(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk = teacher_id)
        return render(request, 'teacher_detail.html', {'teacher': teacher})
    except Teacher.DoesNotExist:
        messages.error(request, _('could not find teacher'))
        return redirect('teacher_list')


def index(request):
    welcome_index= "welcome to index page!"
    return render(request, 'index.html', {'welcome_index': welcome_index})


def uploadfile(request):
    if request.method == 'POST' and request.FILES['myfile']:
        pass
    return redirect('teacher_list')


def upload_csv(csv_file):
    print('------->  uplpad csv method\n')
    print(csv_file)
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Teacher.objects.get_or_create(
                first_name=row[0],
                last_name=row[1],
                email_address=row[3],
                phone_number=row[4],
                room_number=row[5],
                subject_taught=row[6],
            )