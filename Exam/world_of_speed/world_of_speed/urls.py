from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('world_of_speed.common.urls')),
    path('profile/', include('world_of_speed.profiles.urls')),
    path('car/', include('world_of_speed.cars.urls')),
)

