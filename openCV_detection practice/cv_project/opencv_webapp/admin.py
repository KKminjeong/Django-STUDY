from django.contrib import admin
from .models import ImageUploadModel

# Register your models here.
class image_upload_Admin(admin.ModelAdmin):
    list_display = ('description', 'document', )

admin.site.register(ImageUploadModel, image_upload_Admin)
