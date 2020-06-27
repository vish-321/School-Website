from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name = 'mainsite'),
	path('geninfo/', views.geninfo, name = 'geninfo'),
	
]