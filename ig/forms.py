from django import forms
from .models import Pic

class NewPicForm(forms.ModelForm):
    class Meta:
        model = Pic
        exclude = []


# from django.contrib.auth import authenticate, get_user_model

# User = get_user_model()

# class UserLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError('This user does not exist')
#             if not user.check_password(password):
#                 raise forms.ValidationError('Incorrect password')

#         return super(UserLoginForm, self).clean(*args, **kwargs)


# class UserSignUpForm(forms.ModelForm):
#     email = forms.EmailField(label='Email Address')
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password'

#         ]
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         email_qs = User.objects.filter(email=email)
#         if email_qs.exists():
#             raise forms.ValidationError(
#                 'This email is already being used'
#             )
#         return email

