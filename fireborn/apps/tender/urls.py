from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  

app_name = 'tender'

urlpatterns = [
    path('', views.index, name='Tender'),
]
urlpatterns += staticfiles_urlpatterns()
 