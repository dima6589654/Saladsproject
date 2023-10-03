from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    """
    Форма для входа пользователя.
    """
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterUserForm(UserCreationForm):
    """
    Форма для регистрации нового пользователя.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
