from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django_filters import FilterSet, CharFilter, NumberFilter
from django.views.generic import View
from subjects.models import Subject
from locations.models import Location
from .forms import (
				UserProfileForm, 
				UserSignUpForm, 
				TutorFilterForm
				)
from .models import UserProfile
from analytics.mixins import ObjectViewedMixin

User = get_user_model()


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        form_email = form.cleaned_data.get("email")
        from_email = settings.EMAIL_HOST_USER
        message_content = send_mail(
        subject = 'Account activation',
        message = 'Hi there, you have succesfully created your account, please activate your email next. at http://127.0.0.1:8000/accounts/activate/',
        from_email = from_email,
        recipient_list = [form_email,],
        fail_silently=False,
         ) 
        return redirect('login')


class TutorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = UserProfile
	template_name = 'accounts/tutuor_add.html'
	form_class = UserProfileForm
	success_url = "/"

	def get_initial(self):
		initial = super(TutorUpdateView,self).get_initial()
		subjects = self.get_object().subjects.all()
		initial["subjects"] = ", ".join([x.name for x in subjects])
		return initial

	def form_valid(self, form):
		valid_data = super(TutorUpdateView, self).form_valid(form)
		form.instance.user = self.request.user
		subjects = form.cleaned_data.get("subjects")
		tutor = self.get_object()
		tutor.subjects.clear()
		if subjects:
			subject_lists = subjects.split(",")
			for subject in subject_lists:
				if not subject == " ":
					new_subject = Subject.objects.get_or_create(name=str(subject).strip())[0]
					tutor.subjects.add(new_subject)
				new_subject.count += 1
				new_subject.save()
		return valid_data

	def test_func(self):
	    tutor = self.get_object()
	    if self.request.user == tutor.user:
	        return True
	    return False

	def get_context_data(self, *args, **kwargs):
		context = super(TutorUpdateView, self).get_context_data(*args, **kwargs)
		if self.request.user.is_authenticated:
			user = self.request.user
			tutor = get_object_or_404(UserProfile, user=user)
			context["tutor"] = tutor
		context["title"] = 'Home'
		return context


class TutorDetailView(LoginRequiredMixin, View):

	def get(self, request, *args, **kwargs):
		user = self.request.user
		tutor = get_object_or_404(UserProfile, user=user)
		context = {}
		context["tutor"] = tutor
		return render(request, "accounts/tutor_detail.html", context)


class TutorChannelView(ObjectViewedMixin, View):

	def get(self, request, *args, **kwargs):
		user = self.request.user
		tutor = get_object_or_404(UserProfile, user=user)
		context = {}
		context["tutor"] = tutor
		return render(request, "accounts/tutor_detail.html", context)


class TutorChannelView(ObjectViewedMixin, DetailView):
	model = UserProfile
	template_name =  "accounts/tutor_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(TutorChannelView, self).get_context_data(*args, **kwargs)
		tutor = self.get_object()
		context["tutor"] = tutor
		context["title"] = 'Home'
		return context



class TutorFilter(FilterSet):

	work_experience = CharFilter(field_name='work_experience', lookup_expr='icontains', distinct=True)
	sex = CharFilter(field_name='sex', lookup_expr='icontains', distinct=True)
	qualification = CharFilter(field_name='qualification', lookup_expr='icontains', distinct=True)
	class Meta:
		model = UserProfile
		fields = [
			'work_experience',
			'sex',
			'qualification',
		]


class FilterMixin(object):
	filter_class = None
	search_ordering_param = "ordering"

	def get_queryset(self, *args, **kwargs):
		try:
			qs = super(FilterMixin, self).get_queryset(*args, **kwargs)
			return qs
		except:
			raise ImproperlyConfigured("You must have a queryset in order to use the FilterMixin")

	def get_context_data(self, *args, **kwargs):
		context = super(FilterMixin, self).get_context_data(*args, **kwargs)
		qs = self.get_queryset()
		ordering = self.request.GET.get(self.search_ordering_param)
		if ordering:
			qs = qs.order_by(ordering)
		filter_class = self.filter_class
		if filter_class:
			f = filter_class(self.request.GET, queryset=qs)
			context["object_list"] = f.qs.all()
		return context


class TutorListView(FilterMixin, ListView):
	model = UserProfile
	queryset = UserProfile.objects.filter(is_tutor=True)
	paginate_by = 3
	template_name = 'accounts/tutor_list.html'
	filter_class = TutorFilter

	def get_context_data(self, *args, **kwargs):
		context = super(TutorListView, self).get_context_data(*args, **kwargs)
		if self.request.user.is_authenticated:
			user = self.request.user
			tutor = get_object_or_404(UserProfile, user=user)
			context["tutor"] = tutor
		context["title"] = 'Home'
		context["query"] = self.request.GET.get("q")
		context["filter_form"] = TutorFilterForm(data=self.request.GET or None)
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super(TutorListView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = UserProfile.objects.filter(
				Q(first_name__icontains=query) |
				Q(last_name__icontains=query) |
				Q(sex__icontains=query) |
				Q(marital_status__icontains=query) |
				Q(city__name__icontains=query) |
				Q(school__icontains=query) |
				Q(job_position__icontains=query) |
				Q(location__icontains=query) |
				Q(subjects__name__icontains=query) 
				).distinct()
			try:
				qs2 = UserProfile.objects.filter(
					Q(age=query)
				).distinct()
				qs = (qs | qs2).distinct()
			except:
				pass
		return qs
