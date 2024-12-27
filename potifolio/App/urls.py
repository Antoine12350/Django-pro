from django.urls import path
from . import views
from .views import all_members

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('all_members/', views.all_members, name='all_members'),
]
