import boto3

class EC2Service:
    def __init__(self):
        self.ec2 = boto3.client('ec2')

    def attach_iam_role_to_instance(self, role_name, instance_id):
        return self.ec2.associate_iam_instance_profile(
            IamInstanceProfile={'Name': role_name},
            InstanceId=instance_id
        )
