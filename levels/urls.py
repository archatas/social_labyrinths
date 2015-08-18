# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url(r'^$', level_list, name="level_list"),
    url(r'^add/$', add_level, name="add_level"),
    url(r'^(?P<slug>[^/]+)/$', level_detail, name="level_detail"),
    url(r'^(?P<slug>[^/]+)/project.json$', level_project_json, name="level_project_json"),
    url(r'^(?P<slug>[^/]+)/change/$', change_level, name="change_level"),
]
