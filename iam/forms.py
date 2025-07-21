from django import forms

from .models import IAMRoleRequest


class IAMRoleRequestForm(forms.ModelForm):
    class Meta:
        model = IAMRoleRequest
        fields = ['role_name', 'description', 'policy_arn', 'ec2_instance_id']
