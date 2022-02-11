import re
from django import forms
from django.forms import inlineformset_factory
from .models import *
from .options import ACTIVITIES2
from django.utils.safestring import mark_safe
import django_filters
from crispy_forms.helper import FormHelper

DEPARTMENTS_FORM = []
IB_FORM = []
i = 0
for dept in DEPARTMENTS.keys():
    DEPARTMENTS_FORM.append((i,dept))
    i += 1
i = 0
for act in ACTIVITIES2:
    IB_FORM.append((i,act[0]))
    i += 1

class FilterForm(forms.Form):
    # join_year = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'placeholder': "Filter by Joining Year", 'class':'form-control'}), 
    #     help_text="Type the year in the box",
    #     required=False)
    # graduation_year = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'placeholder': "Filter by Graduation Year", 'class':'form-control'}), 
    #     help_text="Type the year in the box",
    #     required=False)
    department = forms.MultipleChoiceField(
        choices= DEPARTMENTS_FORM, 
        widget=forms.SelectMultiple(attrs={'placeholder': "Filter by Department", 'class':'form-control'}), 
        help_text="Hold Ctrl to select/de-select multiple options",
        required=False)
    hostel = forms.MultipleChoiceField(
        choices=Student_Profile.hostel_choices, 
        widget=forms.SelectMultiple(attrs={'placeholder': "Filter by Hostel", 'class':'form-control'}), 
        help_text="Hold Ctrl to select/de-select multiple options",
        required=False)
    ib = forms.MultipleChoiceField(choices=IB_FORM, 
        label="IB / Clubs / Councils",
        widget=forms.SelectMultiple(attrs={'placeholder': "Filter by Club/IB name", 'class':'form-control'}), 
        help_text="Hold Ctrl to select/de-select multiple options",
        required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'

#Necessary for registration
class LoginForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Eg. Dhairya", 'class':'form-control'}), 
        help_text="Your First Name",
        required=True
    )    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Eg. Jain", 'class':'form-control'}), 
        help_text="Enter your last name",
        required=False
    )
    email = forms.CharField(
        min_length=9,
        max_length=9,
        # validators=[validate_email_iitb_domain],
        widget=forms.TextInput(attrs={'placeholder': "Eg. 18b080006", 'class':'form-control'}), 
        help_text="Enter your roll number: Email will be sent to roll-no@iitb.ac.in",
        label="Roll Number",
        required=True
    )
    iitborg = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Eg. dhairyaj or PLEASE leave blank if you don't have one", 'class':'form-control'}), 
        help_text="Enter your iitbombay.org username: Email will be sent to username@iitbombay.org. Use only if you're an alumni, and don't have email forwarding enabled",
        label="Username (iitbombay.org)",
        required=False
    )
    otp_field = forms.CharField(max_length=6, required=False, min_length=6, 
        widget=forms.TextInput(attrs={'placeholder': "eg. 123456 or Leave Blank to Generate a new OTP", 'class':'form-control'}), 
        help_text="Enter the 6 digit OTP you recieved on your email (roll-no@iitb.ac.in). Leave blank to Generate a new OTP",
    )
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', ]
        # widget = forms.TextInput(attrs={'class': "form-control"})

StudentFormSet = inlineformset_factory(Student, Student_Profile,
    fields = ('email', 'address', 'personal_email', 'hostel', 'room_no', 'department', 'program', 'degree', 'join_year', 'graduation_year', 'nickname', 'ib1', 'ib2', 'ib3', 'notification_preference'),
    widgets = {
        'address': forms.TextInput(attrs={'placeholder': "For Yearbook Home Delivery"}), 
        'email': forms.EmailInput(attrs={'placeholder': "For Notifications and Mailing", "readonly": "true"}),
        'personal_email': forms.EmailInput(attrs={'placeholder': "For Extended YB Access"}),
        'ib1': forms.Select(choices=ACTIVITIES2), 
        'ib2': forms.Select(choices=ACTIVITIES2), 
        'ib3': forms.Select(choices=ACTIVITIES2), 
        'department': forms.Select(choices=tuple([(dept, dept) for dept in DEPARTMENTS.keys()])),
        'notification_preference': forms.Select(choices=NOTIFICATION_PREFERENCES, attrs={'placeholder': 'Default is send notification everytime'})
    },
    max_num = 1
)
# widgets = {'ib1': forms.Select(choices=ACTIVITIES2), 'ib2': forms.TextInput(), 'ib3': forms.TextInput(), 'ib4': forms.TextInput(), 'department': forms.TextInput()},


class HorizontalRadioRenderer(forms.RadioSelect):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class SortForm(forms.Form):
    sort_time = forms.ChoiceField(choices=(('1', 'Time'), ('0', 'Likes')),
                               widget=forms.RadioSelect(attrs={'class': 'inline','onchange': 'submit();','class': 'sorting'}))
