from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile
from .utils import (
                SEX_CHOICES,  
                WORK_EXPERIENCE_CHOICES,
                QUALIFICATION_CHOICES
                )

User = get_user_model()


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(
                            widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            max_length=64, 
                            help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
                            ) 
    class Meta(UserCreationForm.Meta):
        model = User

        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save()
        return user


class ContactForm(forms.Form):

    full_name = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Full Name'
             }
         ))

    email = forms.CharField(label='', required=False, widget=forms.EmailInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Email ID'
             }
         ))

    subject = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Subject of your message'
             }
         ))

    message = forms.CharField(
                label='',
                widget=forms.Textarea(
                        attrs={'class': 'form-control resume',
                        'placeholder': 'Enter message to send here.',
                        'rows': 5}
                ))


class UserProfileForm(forms.ModelForm):

    first_name = forms.CharField(
                                    label='', 
                                    required=True, 
                                    widget=forms.TextInput(
                                    attrs={'class':'form-control' , 
                                    'autocomplete': 'off','pattern':'[A-Za-z ]+', 
                                    'title':'Enter Characters Only '}))

    middle_name = forms.CharField(
                                    label='', 
                                    required=True, 
                                    widget=forms.TextInput(
                                    attrs={'class':'form-control' , 
                                    'autocomplete': 'off','pattern':'[A-Za-z ]+', 
                                    'title':'Enter Characters Only '}))

    last_name = forms.CharField(
                                    label='', 
                                    required=True, 
                                    widget=forms.TextInput(
                                    attrs={'class':'form-control' , 
                                    'autocomplete': 'off','pattern':'[A-Za-z ]+', 
                                    'title':'Enter Characters Only '}))

    phone = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Enter International phone format: +233 543334974'
             }
         ))

    email = forms.CharField(label='', required=False, widget=forms.EmailInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Email ID'
             }
         ))

    address = forms.CharField(
                label='',
                widget=forms.Textarea(
                        attrs={'class': 'form-control resume',
                        'placeholder': 'Enter your address here.',
                        'rows': 5}
                ))

    school = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Sunyani Technical University.'
             }
         ))

    year_completed = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': '2020'
             }
         ))

    education_additional_information = forms.CharField(
                label='',
                widget=forms.Textarea(
                        attrs={'class': 'form-control resume',
                        'placeholder': 'Additional Education Information.',
                        'rows': 5}
                ))

    company = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Company Name'
             }
         ))

    job_position = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Job Position'
             }
         ))

    location = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Sunyani'
             }
         ))

    start_date = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': '2020-03-27'
             }
         ))

    end_date = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': '2020-03-27'
             }
         ))

    work_additional_information = forms.CharField(
                label='',
                widget=forms.Textarea(
                        attrs={'class': 'form-control resume',
                        'placeholder': 'Additional Work Information.',
                        'rows': 5}
                ))


    refree_1 = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': ''
             }
         ))


    refree_1_phone = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': ' +233 543334974'
             }
         ))

    refree_2 = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': ''
             }
         ))

    refree_2_phone = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': ' +233 543334974'
             }
         ))

    subjects = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': 'Please seperate with a comma if more than one subject'
             }
         ))

    website = forms.CharField(label='', required=False, widget=forms.TextInput(
             attrs={'class': 'form-control resume',
             'placeholder': ' www.codewithtm.com'
             }
         ))

    
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'profile_image',
            'age',
            'sex',
            'marital_status',
            'city',
            'phone',
            'email',
            'address',
            'school',
            'year_completed',
            'qualification',
            'certificate',
            'education_additional_information',
            'company',
            'job_position',
            'work_experience',
            'salary',
            'website',
            'location',
            'start_date',
            'end_date',
            'resume',
            'work_additional_information',
            'refree_1',
            'refree_1_phone',
            'refree_2',
            'refree_2_phone',
            ]


class TutorFilterForm(forms.Form):

    work_experience = forms.ChoiceField(
      label='',
      choices=WORK_EXPERIENCE_CHOICES, 
      widget=forms.RadioSelect, 
      required=False
      )

    sex = forms.ChoiceField(
      label='',
      choices=SEX_CHOICES, 
      widget=forms.RadioSelect, 
      required=False
      )

    qualification = forms.ChoiceField(
      label='',
      choices=QUALIFICATION_CHOICES, 
      widget=forms.RadioSelect, 
      required=False
      )
















