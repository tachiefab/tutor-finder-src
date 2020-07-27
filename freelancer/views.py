from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.edit import FormMixin
from django.core.mail import send_mail
from locations.models import Location
from subjects.models import  Subject
from accounts.models import UserProfile, Testimonials
from accounts.forms import ContactForm
from django.conf import settings


class IndexView(View):

	def get(self, request, *args, **kwargs):
		locations = Location.objects.all()
		subjects = Subject.objects.all()
		popular_subjects = Subject.objects.order_by('-count')[:8]
		top_rated_tutors = UserProfile.objects.all()[:3]
		testimonies = Testimonials.objects.all()[:3]
		context = {}
		if self.request.user.is_authenticated:
			user = self.request.user
			tutor = get_object_or_404(UserProfile, user=user)
			context["tutor"] = tutor
		context["title"] = 'Home'
		context["locations"] = locations
		context["subjects"] = subjects
		context["popular_subjects"] = popular_subjects
		context["top_rated_tutors"] = top_rated_tutors
		context["testimonies"] = testimonies
		return render(request, "index/index.html", context)


class AboutUsView(View):

	def get(self, request, *args, **kwargs):
		total_tutors = UserProfile.objects.filter(is_tutor=True).count()
		total_users = UserProfile.objects.all().count()
		total_subjects = Subject.objects.all().count()
		total_locations = Location.objects.all().count()
		context = {}
		if self.request.user.is_authenticated:
			user = self.request.user
			tutor = get_object_or_404(UserProfile, user=user)
			context["tutor"] = tutor
		context["title"] = 'About Us'
		context["total_users"] = total_users
		context["total_tutors"] = total_tutors
		context["total_subjects"] = total_subjects
		context["total_locations"] = total_locations
		return render(request, "aboutus/about_us.html", context)

def ContactUsView(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = form.cleaned_data.get("subject")
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email,]
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				subject, 
				form_email)
		some_html_message = form_message
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=False)

	if request.user.is_authenticated:
			user = request.user
			tutor = get_object_or_404(UserProfile, user=user)
			context = {
		"tutor": tutor,
	}
	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
		# "tutor": tutor,
	}
	return render(request, "contactus/contact_us.html", context)
