from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('Offline/', views.offline, name='offline'),
    path('Contact/', views.contact, name='contact'),
]
urlpatterns += staticfiles_urlpatterns()
 