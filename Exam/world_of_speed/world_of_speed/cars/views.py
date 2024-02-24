from django.urls import reverse_lazy
from django.views import generic as views
from world_of_speed.helpers.mixins import CarObjectMixin, CarFormMixin
from world_of_speed.profiles.models import Profile


'''View for the car catalogue. URL: /car/catalogue/'''
class CarCatalogueView(CarObjectMixin, views.ListView):

    template_name = 'cars/catalogue.html'


'''View for creating a car. URL: /car/create/'''
class CarCreateView(CarFormMixin, views.CreateView):

    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('car_catalogue')

    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['image_url'].widget.attrs={'placeholder': 'https://...'}
        return form
    
    def form_valid(self, form):
        form.save(commit=False)
        form.instance.owner_id = Profile.objects.first().pk
        return super().form_valid(form)
    
    
'''View for the details of a car. URL: /car/<int:pk>/details/'''
class CarDetailsView(CarObjectMixin, views.DetailView):

    template_name = 'cars/car-details.html'


'''View for editing a car. URL: /car/<int:pk>/edit/'''
class CarEditView(CarFormMixin, views.UpdateView):

    template_name = 'cars/car-edit.html'
    success_url = reverse_lazy('car_catalogue')


'''View for deleting a car. URL: /car/<int:pk>/delete/'''
class CarDeleteView(CarFormMixin, views.DeleteView):

    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('car_catalogue')


    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object

        return kwargs
    
        
    def get_form(self, form_class=None):

        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = "disabled"
            field.widget.attrs['readonly'] = "readonly"
        
        return form
    
    
    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()

        return self.form_valid(form)
