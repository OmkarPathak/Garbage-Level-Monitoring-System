from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exists')

            if not user.check_password(password):
                raise forms.ValidationError('Password incorrect')

        return super(UserLoginForm, self).clean(*args, **kwargs)


# for registration form
# class UserRegisterForm(forms.ModelForm):
#     email = forms.EmailField(label='Email Address')
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'confirm_password'
#         ]

#     def clean_confirm_password(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError('Passwords do not match')
#         check_email = User.objects.filter(email=email)
#         if check_email.exists():
#             raise forms.ValidationError('This email has already been taken')
#         return email
