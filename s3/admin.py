from django.contrib import admin
from django.contrib.admin import ModelAdmin

from s3.models import UploadedFile, Document


# Register your models here.

@admin.register(UploadedFile)
class UploadedFileAdmin(ModelAdmin):
    list_display = ("pk", "file", "content_type", "file_size")
    list_filter = ("content_type", )

    def file(self, obj):
        if obj.file:
            from s3.services.s3_service import S3Service
            S3Service().get_pre_signed_read_url(
                obj.file.name
            )
            url = S3Service().get_pre_signed_read_url(
                obj.file.name
            )
            from django.utils.html import format_html
            return format_html('<a href="{}" target="_blank">View File</a>', url)
        return "-"

    # file.short_description = "File (Presigned)"

@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    pass
