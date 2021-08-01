import django_filters
from .models import Teacher

class TeacherFilters(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'last_name': ['contains']
        }
