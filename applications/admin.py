from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'status', 'applied_date', 'user')
    list_filter = ('status', 'applied_date')
    search_fields = ('job_title', 'company_name', 'notes')