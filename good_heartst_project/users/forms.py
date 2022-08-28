from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',)
