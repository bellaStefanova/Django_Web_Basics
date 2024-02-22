from django.urls import reverse_lazy
from django.views import generic as views
from .forms import AddAlbumForm
from .models import Album
from my_music_app.helpers.mixins import GetProfileMixin, GetVisibleFieldsOfAlbumMixin


'''Add Album View on localhost:8000/album/add/'''
class AddAlbumView(views.FormView, GetProfileMixin):

    template_name = 'albums/album-add.html'
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile

        return context
    

    def form_valid(self, form):

        album = form.save(commit=False)
        album.owner = self.existing_profile
        album.save()

        return super().form_valid(form)
    
'''Details Album View on localhost:8000/album/<int:pk>/details/'''
class AlbumDetailsView(views.DetailView, GetProfileMixin):

    template_name = 'albums/album-details.html'
    model = Album
    context_object_name = 'album'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile

        return context


'''Edit Album View on localhost:8000/album/<int:pk>/edit/'''
class EditAlbumView(views.UpdateView, GetProfileMixin):

    template_name = 'albums/album-edit.html'
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile

        return context


'''Delete Album View on localhost:8000/album/<int:pk>/delete/'''
class DeleteAlbumView(views.DeleteView, GetProfileMixin, GetVisibleFieldsOfAlbumMixin):

    template_name = 'albums/album-delete.html'
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile

        return context
    

    def get_initial(self):

        initial = super().get_initial()
        album = self.get_object()
        fields = self.visible_fields
        
        for field in fields:
            initial[field] = getattr(album, field)

        return initial
    

    def get_form(self, form_class=None):

        fields = self.visible_fields
        form = super().get_form(form_class)

        form.fields['genre'].widget.attrs['disabled'] = "disabled"
        
        return form
    

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()

        return self.form_valid(form)
    