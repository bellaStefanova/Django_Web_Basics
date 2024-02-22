import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_music_app.settings")
django.setup()

from my_music_app.profiles.models import Profile
from my_music_app.albums.models import Album
from my_music_app.albums.forms import AddAlbumForm
# Profile.objects.all().delete()

# print(Album.objects.first().__dict__)
# print(Profile.objects.first().__dict__)

# for album in Album.objects.all():
#     if album.album_name == 'another test':
#         album.delete()
    # print(album.__dict__)

# print(Album.objects.all())
print(AddAlbumForm.Meta.fields)
print(getattr(AddAlbumForm.Meta, 'fields'))