from django.contrib import admin
from django.urls import path
from myipapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('myip', views.get_user_ip, name='get_user_ip'),  # IP check page
]
