from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.views import generic as views
from .models import Profile
from my_music_app.albums.models import Album


class HomeView(views.FormView):
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
        if Profile.objects.first():
            return render(request, 'profiles/home-with-profile.html', self.get_context_data())
        return render(request, 'profiles/home-no-profile.html', self.get_context_data())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        context['added_albums'] = Album.objects.all()
        return context


    def form_valid(self, form):
        form.save()
        return render(self.request, 'profiles/home-with-profile.html', self.get_context_data())
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class ProfileDetailsView(views.ListView):
    template_name = 'profiles/profile-details.html'
    model = Profile
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        context['albums_count'] = len(Album.objects.filter(owner=Profile.objects.first()))
        return context


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        return context
        
    def get_object(self, queryset=None):
        return Profile.objects.first()
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.form_valid(form)