from django.views import generic as views
from world_of_speed.helpers.mixins import GetProfileMixin


class IndexView(GetProfileMixin, views.TemplateView):

    template_name = 'common/index.html'


