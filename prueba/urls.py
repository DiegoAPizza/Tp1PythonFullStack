from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

   

urlpatterns = [
    path('',views.inicio,name="index"),
    path('login/',views.login,name="login"),
    
]
