from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from .forms import AddAlbumForm
from my_music_app.profiles.models import Profile
from .models import Album


# Create your views here.
class AddAlbumView(views.FormView):
    template_name = 'albums/album-add.html'
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        # context['added_albums'] = Album.objects.all()
        return context
    
    def form_valid(self, form):
        album = form.save(commit=False)
        album.owner = Profile.objects.first()
        album.save()
        return super().form_valid(form)
    

class AlbumDetailsView(views.DetailView):
    template_name = 'albums/album-details.html'
    model = Album
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        return context
    
class EditAlbumView(views.UpdateView):
    template_name = 'albums/album-edit.html'
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        return context


class DeleteAlbumView(views.DeleteView):
    template_name = 'albums/album-delete.html'
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        return context
    
    def get_initial(self):
        initial = super().get_initial()
        album = self.get_object()
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        for field in fields:
            initial[field] = getattr(album, field)
        return initial
    
    def get_form(self, form_class=None):
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        form = super().get_form(form_class)

        form.fields['genre'].widget.attrs['disabled'] = "disabled"

        for field in fields:
            form.fields[field].widget.attrs['readonly'] = "readonly"
        
        return form
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        return self.form_valid(form)
    