from django.conf import settings
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from .utils import (
                SEX_CHOICES, 
                MARITAL_STATUS_CHOICES, 
                WORK_EXPERIENCE_CHOICES,
                QUALIFICATION_CHOICES
                )
from django.db.models.signals import post_save
from locations.models import Location
from subjects.models import Subject
from analytics.models import ObjectViewed
from django.contrib.contenttypes.models import ContentType


def profile_image_upload_location(instance, filename):
    return "%s/profile/%s" %(instance.user.username, filename)

def certificate_upload_location(instance, filename):
    return "%s/certificate/%s" %(instance.user.username, filename)

def resume_upload_location(instance, filename):
    return "%s/resume/%s" %(instance.user.username, filename)

class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_image = models.ImageField(upload_to=profile_image_upload_location, 
            null=True, 
            blank=True)
    age = models.IntegerField(default=10)
    sex = models.CharField(
                                max_length=20,
                                choices=SEX_CHOICES,
                                null=True,
                                blank=True
                                )
    marital_status = models.CharField(
                                max_length=10,
                                choices=MARITAL_STATUS_CHOICES,
                                null=True,
                                blank=True
                                )
    city = models.ForeignKey(Location, related_name='tutor_city', on_delete=models.CASCADE, null=True, blank=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=500)
    address = models.TextField(null=True, blank=True)
    school = models.CharField(max_length=500, null=True, blank=True)
    year_completed = models.BigIntegerField(default=1990,  null=True, blank=True)
    qualification = models.CharField(
                                max_length=50,
                                choices=QUALIFICATION_CHOICES,
                                null=True,
                                blank=True
                                )
    certificate = models.ImageField(upload_to=certificate_upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    education_additional_information = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=500, null=True, blank=True)
    job_position = models.CharField(max_length=500, null=True, blank=True)
    salary = models.BigIntegerField(default=0)
    website = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    work_experience = models.CharField(
                                max_length=50,
                                choices=WORK_EXPERIENCE_CHOICES,
                                null=True,
                                blank=True
                                )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    resume = models.FileField(upload_to=resume_upload_location, 
            null=True, 
            blank=True
            )
    work_additional_information = models.TextField(null=True, blank=True)
    refree_1 = models.CharField(max_length=100, null=True, blank=True)
    refree_1_phone = PhoneNumberField()
    refree_2 = models.CharField(max_length=100, null=True, blank=True)
    refree_2_phone = PhoneNumberField()
    subjects = models.ManyToManyField(Subject, blank=True)
    is_tutor = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ["-first_name"]

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        first_name = self.first_name
        last_name = self.last_name
        if first_name and last_name:
            return first_name + " " + last_name
        else:
            return self.user.username

    def get_absolute_url(self):
        return reverse("profile")

    def get_image_url(self):
        try:
            img = self.profile_image.url
        except:
            img = None
        return img

    def get_resume_url(self):
        try:
            resume = self.resume.url
        except:
            resume = None
        return resume

    def get_subjects(self):
        subject_list = []
        subjects = self.subjects.all()
        for subject in subjects:
            subject_list.append(subject.name)
        return str(subject_list)

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)
post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)



class Testimonials(models.Model):
    user        = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile')
    testimony = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.user.username
