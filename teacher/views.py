from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
import csv
import io
from django.conf import settings
from django.contrib.staticfiles import finders
from .filters import TeacherFilters


def teacher(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher
    }
    if request.method == 'POST' and request.FILES['myfile']:
        if request.user.is_authenticated:
            uploaded_file = request.FILES['myfile'].read().decode('utf-8')
            csv_file = io.StringIO(uploaded_file)
            upload_csv(csv_file)
        else:
            messages.error(request, _('only authenticated users can upload CSV file'))
    else:
        filter = TeacherFilters(request.GET or None, queryset=teacher)
        teacher = filter.qs
        context = {
            'teacher': teacher,
            'filter': filter
        }
    return render(request, 'teacher_list.html', context=context)


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
    print(csv_file)
    for line in csv.reader(csv_file, delimiter=','):
        image_url = '/images/'+line[2]
        teacher = Teacher(
                    first_name=line[0],
                    last_name=line[1],
                    profile_picture=image_url,
                    email_address=line[3],
                    phone_number=line[4],
                    room_number=line[5],
                    subject_taught=line[6],
                )
        teacher.save()
