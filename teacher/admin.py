from django.contrib import admin
from .models import Teacher

class TeacherModelAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'profile_picture', 'email_address', 'phone_number',
              'subject_taught', 'room_number1']
    list_display = ['first_name', 'last_name']
    list_filter = ['room_number1']
    search_fields = ['first_name', 'last_name','phone_number']

admin.site.register(Teacher, TeacherModelAdmin)