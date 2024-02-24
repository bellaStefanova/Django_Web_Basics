from django.db.models.base import Model as Model
from django.forms import modelform_factory
from django.views import generic as views
from world_of_speed.profiles.models import Profile
from world_of_speed.cars.models import Car


'''Mixin for adding the profile of the user to the context of the view.'''
class GetProfileMixin(views.base.ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_profile'] = Profile.objects.first()
        return context
    
    def get_object(self, queryset=None):

        return Profile.objects.first()


'''Mixin for adding the car as object.'''
class CarObjectMixin(GetProfileMixin):
    queryset = Car.objects.all()
    context_object_name = 'cars'

    def get_object(self, queryset=None):

        pk = self.kwargs.get('pk')
        return Car.objects.get(pk=pk)


'''Mixin for creating the car form.'''
class CarFormMixin(CarObjectMixin):
    form_class = modelform_factory(Car, fields=['type', 'model', 'year', 'image_url', 'price'])

