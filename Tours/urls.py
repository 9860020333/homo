from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from about.views import about_view
from Home.views import PackagesView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('payment/', include('epay.urls')),
    path('home/', include('Home.urls')),
    path('login/', include('Signup.urls')),
    path('login/', include('Login.urls')),
    path('about/', about_view, name='about'),
    path('packages/', PackagesView, name='packages'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
