from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    bio = models.TextField()
    career_goals = models.TextField()
    email = models.EmailField()
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    year_attended = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.school} - {self.degree}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name