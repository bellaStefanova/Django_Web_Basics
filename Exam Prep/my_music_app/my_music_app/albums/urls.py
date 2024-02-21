from django.urls import path
from .views import AddAlbumView, AlbumDetailsView, EditAlbumView, DeleteAlbumView


urlpatterns=(
    path('add/', AddAlbumView.as_view(), name='add_album'),
    path('<int:pk>/details/', AlbumDetailsView.as_view(), name='album_details'),
    path('<int:pk>/edit/', EditAlbumView.as_view(), name='edit_album'),
    path('<int:pk>/delete/', DeleteAlbumView.as_view(), name='delete_album'),
)