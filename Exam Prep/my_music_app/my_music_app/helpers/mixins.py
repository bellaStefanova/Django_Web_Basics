from django.shortcuts import render
from my_music_app.profiles.models import Profile


'''Mixin for getting the profile of the user, all of his albums and a default
render of template when logged in.'''
class GetProfileMixin:

    template_name_when_logged_in = None

    @property
    def existing_profile(self):

        return Profile.objects.first()
    

    @property
    def all_albums_of_user(self):

        if not self.existing_profile:
            return None
        
        return Profile.objects.first().albums.all()
    

    def get_when_logged_in(self, request):

        return render(request, self.template_name_when_logged_in, self.get_context_data())


'''Mixin for getting the visible fields of the album form.'''
class GetVisibleFieldsOfAlbumMixin:

    form_class = None


    @property
    def visible_fields(self):
        return getattr(self.form_class.Meta, 'fields')

  