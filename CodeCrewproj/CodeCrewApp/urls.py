from django.urls import path
from . import views

# the url that goes to the page for the user

urlpatterns=[
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('gallery/',views.gallery,name='gallery'),
    path('resources/',views.resources,name='resources'),

]