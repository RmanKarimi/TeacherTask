from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, null=False, blank= False, verbose_name=_('last name'))
    profile_picture = models.ImageField(blank=True, verbose_name=_('Profile Picture'), upload_to='images')
    email_address = models.EmailField(verbose_name=_('Email Address'), unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Phone Numbber'))
    room_number = models.IntegerField(default='1', null=True, blank=True, verbose_name=_('Room Number'))
    subject_taught = models.TextField(verbose_name=_('Subject Tought'), null=True, blank=True)

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return self.first_name+ ' ' + self.last_name


    def save(self, **kwargs):
        if len(self.subject_taught.split(',')) > 5:
            print('more than 5 subjects')
            raise ValueError('Adding more than 5 subject for a teacher is not allowed')
        else:
            super(Teacher, self).save(**kwargs)
