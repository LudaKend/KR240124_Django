from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'company', 'phone', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
