from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

   

urlpatterns = [
    path('',views.inicio,name="index"),
    path('login2/',views.login_prueba,name="login2"),
    path('login/',views.login,name="login"),
    
]
urlpatterns += staticfiles_urlpatterns()