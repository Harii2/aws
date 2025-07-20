from django.db.models.signals import post_delete
from django.dispatch import receiver

from s3.models import UploadedFile
from .services.s3_service import S3Service


@receiver(post_delete, sender=UploadedFile)
def delete_file_from_s3(sender, instance, **kwargs):
    if instance.file:
        file_key = instance.file.name
        s3_service = S3Service()
        print("file_key: ", file_key)
        s3_service.delete_s3_object("media/" + file_key)
        print(f"✅ S3 file deleted via signal: {file_key}")
