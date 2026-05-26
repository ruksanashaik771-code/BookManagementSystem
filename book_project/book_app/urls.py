from django.contrib import admin
from django.urls import path
from .views import home_page, profile_page, contact_page, skills_page,proj_page,marks_page,add_user

urlpatterns = [
    path('home/',home_page),
    path("profile/",profile_page),
    path("contacts/",contact_page),
    path('skills/',skills_page),
    path('proj/',proj_page),
    path('marks/',marks_page),
    path('user_form/', add_user),
]