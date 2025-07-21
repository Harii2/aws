# Create your models here.
# Register your models here.
from django.contrib.auth.models import User
from django.db import models


class IAMRoleRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('CREATED', 'Created in AWS'),
    ]

    role_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    policy_arn = models.CharField(max_length=255)  # e.g., AmazonS3FullAccess
    ec2_instance_id = models.CharField(max_length=50)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_iam_requests')

    def __str__(self):
        return f"{self.role_name} ({self.status})"
