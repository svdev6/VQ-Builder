#Django rest-framework
from rest_framework import routers

#Django 
from django.contrib import admin
from django.urls import path, include

#Local Application
from vqbuilder_userstories.views import queries_viewset, saved_queries_viewset

#Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'query-builder', queries_viewset)
router.register(r'saved-queries', saved_queries_viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('vqbuilder_userstories.urls')),
    path('api/', include(router.urls)),
]
