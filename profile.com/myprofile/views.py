from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *

def home(request):
    
    persons = Person.objects.all()
    educations = Education.objects.all()
    languages = Language.objects.all()
    profiles = Profile.objects.all()
    experiences = Experience.objects.all()
    skills = Skills.objects.all()
    interests = Interest.objects.all()
    
    context = {
        'persons':persons,
        'educations':educations,
        'languages':languages, 
        'profiles':profiles,
        'experiences':experiences,
        'skills':skills,
        'interests':interests,
        }
    return render(request, 'profile/home.html', context)



def login_user(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('add')
        else:
            return redirect('login')
    else:
        return render(request, 'profile/login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('home')


def signup_user(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
 
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        print(uname,email,pass1,pass2)
        return redirect('login')

    return render(request, 'profile/signup.html', {} )


def add(request):

    if request.method == "POST":
        personform = PersonForm(request.POST)
        educateform = EducationForm(request.POST)
        languageform = LanguageForm(request.POST)
        profileform = ProfileForm(request.POST)
        experienceform = ExperienceForm(request.POST)
        skillform = SkillsForm(request.POST)
        interestform = InterestForm(request.POST)
        
        if personform.is_valid() and educateform.is_valid() and languageform.is_valid() and profileform.is_valid() and experienceform.is_valid() and skillform.is_valid() and interestform.is_valid():
            personform.save()
            educateform.save()
            languageform.save()
            profileform.save()
            experienceform.save()
            skillform.save()
            interestform.save()

            return redirect('home')
    else:
        personform = PersonForm()
        educateform = EducationForm()
        languageform = LanguageForm()
        profileform = ProfileForm()
        experienceform = ExperienceForm()
        skillform = SkillsForm()
        interestform = InterestForm()

    personform = PersonForm
    educateform = EducationForm
    languageform = LanguageForm
    profileform = ProfileForm
    experienceform = ExperienceForm
    skillform = SkillsForm
    interestform = InterestForm()
        
    return render(request, 'profile/add.html', {'personform':personform, 'educateform':educateform, 'languageform':languageform, 'profileform':profileform, 'experienceform':experienceform, 'skillform':skillform, 'interestform':interestform})


def education(request):

    if request.method == "POST":
        educateform = EducationForm(request.POST)
        
        if educateform.is_valid():
            educateform.save()
            return redirect('home')
    else:
        educateform = EducationForm()

    educateform = EducationForm
    return render(request, 'profile/education.html', {'educateform':educateform})

def language(request):

    if request.method == "POST":
        languageform = LanguageForm(request.POST)
        
        if languageform.is_valid():
            languageform.save()
            return redirect('home')
    else:
        languageform = LanguageForm()

    languageform = LanguageForm
    return render(request, 'profile/language.html', {'languageform':languageform})

def experience(request):

    if request.method == "POST":
        experienceform = ExperienceForm(request.POST)
        
        if experienceform.is_valid():
            experienceform.save()
            return redirect('home')
    else:
        experienceform = ExperienceForm()

    experienceform = ExperienceForm
    return render(request, 'profile/experience.html', {'experienceform':experienceform})


def skill(request):

    if request.method == "POST":
        skillform = SkillsForm(request.POST)
        
        if skillform.is_valid():
            skillform.save()
            return redirect('home')
    else:
        skillform = SkillsForm()

    skillform = SkillsForm
    return render(request, 'profile/skill.html', {'skillform':skillform})

def interest(request):

    if request.method == "POST":
        interestform = InterestForm(request.POST)
        
        if interestform.is_valid():
            interestform.save()
            return redirect('home')
    else:
        interestform = InterestForm()

    interestform = InterestForm

        
    return render(request, 'profile/interest.html', {'interestform':interestform})