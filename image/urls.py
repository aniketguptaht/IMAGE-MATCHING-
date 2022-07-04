
from django.urls import re_path
from .views import DisplayView
app_name = 'images'
urlpatterns = [
    re_path(r'display/$', DisplayView.as_view())
]
