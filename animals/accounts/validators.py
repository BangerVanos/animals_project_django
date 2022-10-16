from django.core.exceptions import ValidationError
import os


def check_photo_file_extension(file):
    extension = os.path.splitext(file.name)[1]  # returns extension
    valid_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.svg', '.tiff']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsupported image extension')
