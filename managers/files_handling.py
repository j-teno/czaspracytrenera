from django.conf import settings
from django.core.files.storage import FileSystemStorage
from os.path import join


def upload_photo(file):
    photos_location = join(settings.MEDIA_ROOT, 'photos')
    fs = FileSystemStorage(location=photos_location, base_url='media/photos/')
    filename = fs.save(file.name, file)
    return filename
