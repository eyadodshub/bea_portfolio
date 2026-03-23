from django.shortcuts import render, redirect
from .models import Profile, Skill, Project, Education, ContactMessage


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()[:3]
    education = Education.objects.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'education': education,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/about.html', {'profile': profile})


def skills(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skills.html', {'skills': skills})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def education(request):
    education = Education.objects.all()
    return render(request, 'portfolio/education.html', {'education': education})


def contact(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        return redirect('contact')  # prevents resubmitting form

    return render(request, 'portfolio/contact.html', {'profile': profile})