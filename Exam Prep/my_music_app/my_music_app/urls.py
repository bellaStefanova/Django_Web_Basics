from django.contrib import admin
from django.urls import include, path
from my_music_app.profiles.views import  HomeView

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('profile/', include('my_music_app.profiles.urls')),
    path('album/', include('my_music_app.albums.urls')),
)
