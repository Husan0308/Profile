from django.urls import path
from . import views


urlpatterns = [
    path('', views.signup_user, name="signup"),
    path('login/', views.login_user, name="login"),
    path('home/', views.home, name="home"),    
    path('add/', views.add, name="add"),
    path('education/', views.education, name="education"),
    path('language/', views.language, name="language"),
    path('experience/', views.experience, name="experience"),
    path('skill/', views.skill, name="skill"),
    path('interest/', views.interest, name="interest"),
]