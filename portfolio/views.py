from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Profile, Skill, Project, Education, ContactMessage


def home(request):
    profile  = Profile.objects.first()
    skills   = Skill.objects.all()
    projects = Project.objects.all()[:3]
    education = Education.objects.all()
    return render(request, 'portfolio/home.html', {
        'profile': profile, 'skills': skills,
        'projects': projects, 'education': education,
    })


def about(request):
    profile = Profile.objects.first()
    skills  = Skill.objects.all()
    return render(request, 'portfolio/about.html', {'profile': profile, 'skills': skills})


def skills(request):
    return render(request, 'portfolio/skills.html', {'skills': Skill.objects.all()})


def projects(request):
    return render(request, 'portfolio/projects.html', {'projects': Project.objects.all()})


def education(request):
    return render(request, 'portfolio/education.html', {'education': Education.objects.all()})


def contact(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Save to database
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        # ── Send SMTP email notification ─────────────────────────────────────
        recipient = getattr(settings, 'CONTACT_RECIPIENT', '') or getattr(settings, 'EMAIL_HOST_USER', '')
        if recipient and getattr(settings, 'EMAIL_HOST_USER', ''):
            try:
                send_mail(
                    subject=f'[Portfolio Contact] {subject}',
                    message=(
                        f'New message from your portfolio contact form.\n\n'
                        f'Name   : {name}\n'
                        f'Email  : {email}\n'
                        f'Subject: {subject}\n\n'
                        f'Message:\n{message}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient],
                    fail_silently=True,
                )
            except Exception:
                pass  # Message is saved to DB regardless of email success

        messages.success(request, "Your message has been sent! I'll get back to you soon.")
        return redirect('contact')

    return render(request, 'portfolio/contact.html', {'profile': profile})
