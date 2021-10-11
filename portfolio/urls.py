from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('contactinfo/', views.contact_information, name='contact_information'),
    path('aboutme/', views.about_me, name='about_me'),
]