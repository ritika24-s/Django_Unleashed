from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='blog_post_list'),
    path('<year>/<month>/<slug>/')
]