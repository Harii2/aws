from django.contrib import admin

from .models import IAMRoleRequest
from .services.role_request_service import RoleRequestService


def approve_and_create_in_aws(self, request, queryset):
    service = RoleRequestService()
    for role_request in queryset.filter(status='PENDING'):
        service.approve(role_request, request.user)


@admin.register(IAMRoleRequest)
class IAMRoleRequestAdmin(admin.ModelAdmin):
    list_display = ['role_name', 'status', 'requested_by', 'created_at']
    actions = ['approve_and_create_in_aws']
