from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name= 'base'),
    path('register/',views.CoachRegistration.as_view(),name='register')
]