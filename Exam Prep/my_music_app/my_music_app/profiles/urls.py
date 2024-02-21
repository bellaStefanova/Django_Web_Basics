from django.urls import path
from .views import ProfileDetailsView, DeleteProfileView


urlpatterns = [
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('delete/', DeleteProfileView.as_view(), name='profile_delete'),
]