from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  

app_name = 'store'

urlpatterns = [
    path('', views.index, name='Store'),
]
urlpatterns += staticfiles_urlpatterns()
 