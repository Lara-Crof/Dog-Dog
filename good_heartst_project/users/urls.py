from django.urls import path, include

from views import CreateView

app_name = 'users'

urlpatterns = [
    path('signup/', CreateView.as_view(), name='sign_up'),
]
