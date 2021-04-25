from django.contrib import admin
from django.urls import path, include
from fuelnet import settings
from django.conf.urls import url

from mobile_app import views
from register import views as v

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mobile_app.urls')),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
]


urlpatterns += staticfiles_urlpatterns()
