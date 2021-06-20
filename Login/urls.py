from django.urls import path
from .views import Logout_View,Login_View
urlpatterns = [ 
    path('',Login_View,name='login'),
    path('logout',Logout_View,name='logout'),
]