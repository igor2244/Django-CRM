from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'email', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'first_name', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'last_name', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'username'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="username_span"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'password1'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="password1"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'password2'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="password2_span"><small>Enter the same password as before, for verification.</small></span>'	


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"first_name"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"last_name"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"email"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"phone"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"address"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"city"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"state"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"zipcode"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)
