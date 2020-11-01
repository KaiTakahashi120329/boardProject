from django.urls import path
from .views import signupFunc, loginFunc

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login')
]
