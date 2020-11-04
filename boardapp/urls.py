from django.urls import path
from .views import signupFunc, loginFunc, listFunc, logoutFunc

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login'),
    path('logout/', logoutFunc, name='logout'),
    path('list/', listFunc, name='list'),
]
