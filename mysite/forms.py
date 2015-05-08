from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    retype_password = forms.CharField(label='retype_password', max_length=100)
    email = forms.CharField(label='email', max_length=100)

    def validate(self):
        return self.password == self.retype_password and self.username and self.email