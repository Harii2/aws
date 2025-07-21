from django.utils import timezone

from .ec2_service import EC2Service
from .iam_service import IAMService


class RoleRequestService:
    def __init__(self):
        self.iam_service = IAMService()
        self.ec2_service = EC2Service()

    def approve(self, role_request, admin_user):
        role_name = role_request.role_name

        # 1. Create Role & Attach Policy
        self.iam_service.create_role(role_name, role_request.description)
        self.iam_service.attach_policy(role_name, role_request.policy_arn)

        # 2. Create instance profile if missing
        self.iam_service.ensure_instance_profile(role_name)

        # 3. Attach profile to EC2
        self.ec2_service.attach_iam_role_to_instance(role_name, role_request.ec2_instance_id)

        # 4. Mark role request as completed
        role_request.status = 'CREATED'
        role_request.reviewed_by = admin_user
        role_request.reviewed_at = timezone.now()
        role_request.save()
