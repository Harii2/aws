# Create your models here.
import mimetypes
import uuid

from django.db import models


def upload_to_s3_unique(instance, filename):
    name, ext = filename.split('.')
    unique_id = uuid.uuid4().hex
    return f"uploads/{name}_{unique_id}.{ext}"

from django.core.exceptions import ValidationError

def validate_file_size(file):
    mb_size = 10
    max_size = mb_size * 1024 * 1024  # 500 MB in bytes
    if file.size > max_size:
        raise ValidationError(f"File size must be under {mb_size} MB.")


class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to_s3_unique, validators=[validate_file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    file_size = models.BigIntegerField(null=True, blank=True)
    content_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
            self.content_type = mimetypes.guess_type(self.file.name)[0] or 'application/octet-stream'
        super().save(*args, **kwargs)