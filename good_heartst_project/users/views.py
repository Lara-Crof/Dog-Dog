from django.views.generic import CreateView
from django.urls import reverse_lazy

from forms import UserCreationForm


class SignUp(CreateView):
    forms = UserCreationForm
    success_url = reverse_lazy('animals/index.html')
    template_name = 'users/signup.html'
