from django.urls import reverse_lazy
from .forms import ProfileForm
from django.views import generic as views
from .models import Profile
from my_music_app.helpers.mixins import GetProfileMixin


'''Home view without URL'''
class HomeView(views.FormView, GetProfileMixin):

    form_class = ProfileForm
    template_name = 'profiles/home-no-profile.html'
    template_name_when_logged_in = 'profiles/home-with-profile.html'


    def get(self, request, *args, **kwargs):

        if not self.existing_profile:
            return super().get(request, *args, **kwargs)
        
        return super().get_when_logged_in(request)
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile
        context['added_albums'] = self.all_albums_of_user

        return context


    def form_valid(self, form):

        form.save()
        request = self.request

        return super().get_when_logged_in(request)
    

    def get_success_url(self):

        return reverse_lazy('home')


'''Profile details view on localhost:8000/profiles/details/'''
class ProfileDetailsView(views.DetailView, GetProfileMixin):

    template_name = 'profiles/profile-details.html'
    model = Profile
    context_object_name = 'profile'
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile
        context['albums_count'] = len(self.all_albums_of_user)

        return context
    
    def get_object(self, queryset=None):

        return self.existing_profile


'''Profile delete view on localhost:8000/profiles/delete/'''
class DeleteProfileView(views.DeleteView, GetProfileMixin):

    template_name = 'profiles/profile-delete.html'
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['existing_profile'] = self.existing_profile

        return context
        

    def get_object(self, queryset=None):

        return self.existing_profile
    

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()

        return self.form_valid(form)