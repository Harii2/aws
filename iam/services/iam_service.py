import json

import boto3


class IAMService:
    def __init__(self):
        self.iam = boto3.client('iam')

    def create_role(self, role_name, description):
        trust_policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        }

        return self.iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description=description
        )

    def attach_policy(self, role_name, policy_arn):
        return self.iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )

    def ensure_instance_profile(self, role_name):
        try:
            self.iam.get_instance_profile(InstanceProfileName=role_name)
        except self.iam.exceptions.NoSuchEntityException:
            self.iam.create_instance_profile(InstanceProfileName=role_name)
            self.iam.add_role_to_instance_profile(
                InstanceProfileName=role_name,
                RoleName=role_name
            )
