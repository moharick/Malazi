from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_warden = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    student_name = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    enrollment_no = models.CharField(max_length=10, unique=True, null=True)
    course = models.ForeignKey(
        'Course',
        null=True,
        default=None,
        on_delete=models.CASCADE)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    room = models.OneToOneField(
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    room_allotted = models.BooleanField(default=False)
    no_dues = models.BooleanField(default=True)

    def __str__(self):
        return self.enrollment_no