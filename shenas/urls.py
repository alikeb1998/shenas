"""shenas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from shenasapp import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register(r'api/userForm', views.UserViewSet)
router.register(r'api/uploadPersonalImage', views.personalImageView)
router.register(r'api/uploadNationalCardImage', views.nationalCardImageView)
router.register(r'api/uploadShenasnameImage', views.shenasnameImageView)



admin.autodiscover()

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^', include(router.urls)),


                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.jwt')),


                  path("api/accounts/", include("shenasapp.urls"))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
