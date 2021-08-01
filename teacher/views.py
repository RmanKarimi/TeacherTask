from django.shortcuts import render, redirect
from .models import Teacher
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
import csv
import io
from django.conf import settings
from .filters import TeacherFilters


def teacher(request):
    teacher = Teacher.objects.all()
    context = {
        'teacher': teacher
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                uploaded_file = request.FILES['myfile'].read().decode('utf-8')
                csv_file = io.StringIO(uploaded_file)
                if upload_csv(csv_file, request) is not None:
                    messages.info(request,_('CSV file uploaded successfully'))
                else:
                    messages.error(request, _('Something happened'))
            except:
                messages.error(request, _('Error reading the file'))
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


def upload_csv(csv_file, request):
    try:
        csvreader= csv.reader(csv_file, delimiter=',')
        next(csvreader)
        for line in csvreader:
            if line[0] and line[1] and line[3] and line[4] and line[6]:
                image_url = '/images/'+line[2]
                teacher = Teacher.objects.get_or_create(
                            first_name=line[0],
                            last_name=line[1],
                            profile_picture=image_url,
                            email_address=line[3],
                            phone_number=line[4],
                            room_number1=line[5],
                            subject_taught=line[6],
                        )
        return True
    except ValueError:
        message= 'Adding more than 5 subject for a teacher is not allowed\n'+str(line[6])
        messages.error(request=request,message=_(message))
        return None
