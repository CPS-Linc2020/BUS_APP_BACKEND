from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [path("admin/", admin.site.urls), path("bus/", include("api.v1.urls"))]
