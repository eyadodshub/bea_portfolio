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
    proficiency = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects/", blank=True, null=True, help_text="Upload a screenshot or preview image for this project")
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    DEGREE_CHOICES = [
        ('bs', 'Bachelor of Science'),
        ('ba', 'Bachelor of Arts'),
        ('hs', 'Senior High School'),
        ('ms', 'Master\'s Degree'),
        # Add more if needed
    ]

    school = models.CharField(max_length=200, verbose_name="School / University")
    degree = models.CharField(max_length=150)
    major = models.CharField(max_length=150, blank=True, null=True, verbose_name="Field / Major")
    start_year = models.CharField(max_length=4)   # e.g. "2023"
    end_year = models.CharField(max_length=10, blank=True, null=True)  # e.g. "PRESENT" or "2025"
    location = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-start_year']   # Newest first

    def __str__(self):
        return f"{self.degree} - {self.school}"

    @property
    def year_range(self):
        if self.end_year:
            return f"{self.start_year} – {self.end_year}"
        return self.start_year


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name