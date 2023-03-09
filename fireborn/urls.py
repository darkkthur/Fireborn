"""fireborn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns +=  (
    path('', include('home.urls', namespace='Home')),
    path('Article/', include('article.urls', namespace='Article')),
    path('News/', include('news.urls', namespace='News')),
    path('Products/', include('products.urls', namespace='Products')),
    path('Service/', include('service.urls', namespace='Service')),
    path('Store/', include('store.urls', namespace='Store')),
    path('Support/', include('support.urls', namespace='Support')),
    path('Tender/', include('tender.urls', namespace='Tender')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 