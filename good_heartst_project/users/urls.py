from django.urls import path, include

from . import views as vw

app_name = 'users'

urlpatterns = [
    path('signup/', vw.SignUp.as_view
         (template_name='users/signup.html'),
         name='signup'
         ),
]
