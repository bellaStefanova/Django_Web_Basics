from django.urls import path
from .views import ProfileCreateView, ProfileDetailsView, ProfileEdit, ProfileDeleteView


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('edit/', ProfileEdit.as_view(), name='profile_edit'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]