from django import forms

class SubmitUser(forms.Form):
    email = forms.EmailField(max_length=100)
    timezone = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class SubmitCalender(forms.Form):
    calender=forms.CharField(max_length=250)
    description = forms.CharField(max_length=250)


class Auth(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

class User_signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User_signup
        fields = ['email','first_name','last_name','password']






