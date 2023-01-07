from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from rol.views import RolList
from rol.views import RolDetail



urlpatterns = [
    re_path(r'^rol/$', RolList.as_view()),
    re_path(r'^rol/(?P<pk>\d+)$', RolDetail.as_view()),
]