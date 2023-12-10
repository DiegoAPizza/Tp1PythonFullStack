from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name="index"),
    path('login/',views.login,name="login"),
    path('service/',views.service,name="service"),
    path('edit/',views.edit,name="edit"),
    path('contactanos/',views.contactanos,name="contactanos"),
    path('blog/',views.blog ,name="blog"),
    path('adn/',views.adn ,name="adn"),
    path('nt/',views.nt ,name="nt"),
    path('servicios/',views.servicios ,name="servicios"),
]
