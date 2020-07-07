# from django.shortcuts import render
# from django.test import override_settings, SimpleTestCase
from django.urls import path
from . import views
from django.conf.urls import handler404, handler500



# import frontend
app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('addmessage/', views.addmessage, name='addmessage'),
    path('addsubscribers/', views.addsubscribers, name='addsubscribers'),
    path('view_cv/', views.view_cv, name='view_cv'),

]
