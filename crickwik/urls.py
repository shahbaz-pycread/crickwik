from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cric-home'),
    path('about/',views.about,name='cric-about'),
]