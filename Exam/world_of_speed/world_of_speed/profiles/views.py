from django import forms
from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views
from .models import Profile
from django.db.models import Sum
from world_of_speed.helpers.mixins  import GetProfileMixin


'''View for creating a profile. URL: /profile/create/'''
class ProfileCreateView(views.CreateView):

    queryset = Profile.objects.all()
    form_class = modelform_factory(Profile, fields=['username', 'email', 'age', 'password'])
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('car_catalogue')


    def get_form(self, form_class=None):
        
        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput()
        form.fields['age'].help_text = 'Age requirement: 21 years and above.'

        return form
    
    
'''View for the details of a profile. URL: /profile/details/'''
class ProfileDetailsView(GetProfileMixin, views.DetailView):

    template_name = "profiles/profile-details.html"
    

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['price'] = Profile.objects.first().cars.all().aggregate(price=Sum('price'))['price']

        return context


'''View for editing a profile. URL: /profile/edit/'''
class ProfileEdit(GetProfileMixin, views.UpdateView):

    template_name = "profiles/profile-edit.html"
    form_class = modelform_factory(Profile, 
                                   fields=['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture'])
    success_url = reverse_lazy('profile_details')
    

    def get_form(self, form_class=None):

        form = super().get_form(form_class)
        form.fields['password'].widget = forms.PasswordInput(render_value=True)

        return form
    

'''View for deleting a profile. URL: /profile/delete/'''
class ProfileDeleteView(GetProfileMixin, views.DeleteView):

    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy('index')


