from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  

app_name = 'support'

urlpatterns = [
    path('', views.index, name='Support'),
]
urlpatterns += staticfiles_urlpatterns()
 