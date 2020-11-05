from django.urls import path
from .views import signupFunc, loginFunc, listFunc, logoutFunc, detailFunc, goodFunc, readFunc

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login'),
    path('logout/', logoutFunc, name='logout'),
    path('list/', listFunc, name='list'),
    path('detail/<int:pk>', detailFunc, name='detail'),
    path('good/<int:pk>', goodFunc, name='good'),
    path('read/<int:pk>', readFunc, name='read')
]
