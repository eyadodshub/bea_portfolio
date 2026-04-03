from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Education, ContactMessage


# ── Admin site branding ──────────────────────────────────────────────────────
admin.site.site_header = "Bea's Portfolio Admin"
admin.site.site_title  = "Portfolio Admin"
admin.site.index_title = "Portfolio Management Panel"


# ── Profile ──────────────────────────────────────────────────────────────────
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'tagline')

    def has_add_permission(self, request):
        return not Profile.objects.exists()


# ── Skill ────────────────────────────────────────────────────────────────────
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'proficiency')
    list_editable = ('proficiency',)


# ── Project ──────────────────────────────────────────────────────────────────
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'technologies', 'image_preview', 'github_link')
    fields        = ('title', 'description', 'technologies', 'image', 'github_link')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:48px;border-radius:6px;object-fit:cover;" />',
                obj.image.url
            )
        return '—'
    image_preview.short_description = 'Preview'


# ── Education ────────────────────────────────────────────────────────────────
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'major', 'start_year', 'end_year')


# ── Contact Messages ─────────────────────────────────────────────────────────
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message')

    def has_add_permission(self, request):
        return False
