from django.contrib import admin
from django.contrib.admin import ModelAdmin

from s3.models import UploadedFile, Document



# Register your models here.

@admin.register(UploadedFile)
class UploadedFileAdmin(ModelAdmin):
    list_display = ("pk", "file", "content_type", "file_size")
    list_filter = ("content_type", )

@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    pass
