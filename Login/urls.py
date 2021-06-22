from django.urls import path
from .views import Logout_View,Login_View,Profile_View,signup_view
urlpatterns = [ 
    path('',Login_View,name='login'),
    path('logout',Logout_View,name='logout'),
    # path('profile', Profile_View, name ='profile'),
    path('signup',signup_view,name='signup'),
]