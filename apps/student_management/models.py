import uuid
from django.db import models

class Student(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    SCHOOL_CHOICES = (
        ("1", "1 Class"),
        ("2", "2 Class"),
        ("3", "3 Class"),
        ("4", "4 Class"),
        ("5", "5 Class"),
        ("6", "6 Class"),
        ("7", "7 Class"),
        ("8", "8 Class"),
        ("9", "9 Class"),
        ("10", "10 Class"),
        ("11", "11 Class"),
        ("12", "12 Class"),
    )

    ENROLLMENT_STATUS_CHOICES = (
        ("active", "Active"),
        ("disabled", "Disabled"),
        ("graduated", "Graduated"),
        ("transferred", "Transferred")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    birth_date = models.DateField("Birth Date")
    gender = models.CharField("Gender", max_length=10, choices=GENDER_CHOICES, default='M')
    current_school_level = models.CharField("Current Class", max_length=20, choices=SCHOOL_CHOICES,)
    enrollment_status = models.CharField("Enrollment Status", max_length=30, choices=ENROLLMENT_STATUS_CHOICES)
    photo = models.ImageField("Photo", upload_to="student_photos", blank=True, null=True)

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        from datetime import datetime
        today = datetime.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age