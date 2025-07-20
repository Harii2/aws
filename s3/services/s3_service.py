import boto3
from django.conf import settings


class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )
        self.bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    def get_pre_signed_read_url(self, file_key: str, expires_in=3600):
        return self.s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': self.bucket_name,
                'Key': file_key
            },
            ExpiresIn=expires_in
        )

    def delete_s3_object(self, file_key: str ):
        return self.s3.delete_object(
            Bucket=self.bucket_name,
            Key=file_key
        )
