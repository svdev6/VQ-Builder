"""
URLs for user_stories_feature
"""

#django
from django.urls import path

#Local Application
from vqbuilder_userstories import views

#Define the application routes
urlpatterns = [
    path('', views.vq_builder_view, name = 'view_query'),
    path('show_queries/', views.show_saved_queries_view, name = 'show_queries'),
]
