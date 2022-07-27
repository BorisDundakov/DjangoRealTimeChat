from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# using UserCreationForm Template
class SignUpForm(UserCreationForm):
    # options class below
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
