from django.db import models
from django.conf import settings


class JobApplication(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'APPLIED', 'Applied'
        INTERVIEWING = 'INTERVIEWING', 'Interviewing'
        OFFER = 'OFFER', 'Offer Received'
        REJECTED = 'REJECTED', 'Rejected'
        ACCEPTED = 'ACCEPTED', 'Accepted'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    company_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    job_url = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.APPLIED
    )
    applied_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-applied_date']

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.get_status_display()})"