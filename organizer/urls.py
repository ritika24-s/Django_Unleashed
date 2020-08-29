from django.urls import path

from .views import *

urlpatterns = [
    path('tag/<slug>/', tag_detail, name='organizer_tag_detail'),
    path('tag/', tag_list, name='organizer_tag_list'),
    path('startup/<slug>/', startup_detail, name='organizer_startup_detail'),
    path('startup/', startup_list, name='organizer_startup_list'),
]