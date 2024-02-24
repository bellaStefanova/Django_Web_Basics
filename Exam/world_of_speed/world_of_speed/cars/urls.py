from django.urls import path
from .views import CarCatalogueView, CarCreateView, CarDetailsView, CarEditView, CarDeleteView


urlpatterns=(
    path('catalogue/', CarCatalogueView.as_view(), name='car_catalogue'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('<int:pk>/details/', CarDetailsView.as_view(), name='car_details'),
    path('<int:pk>/edit/', CarEditView.as_view(), name='car_edit'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
)