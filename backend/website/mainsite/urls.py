from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name = 'mainsite'),
	path('geninfo/', views.geninfo, name = 'geninfo'),
	path('sctu/', views.sctu, name = 'sctu'),
	path('infra/', views.infra, name = 'infra'),
	path('prmsg/', views.prmsg, name = 'prmsg'),
	path('procedure/', views.procedure, name = 'procedure'),
	path('age/', views.age, name = 'age'),
	path('academic/', views.academic, name = 'academic'),
	path('others/', views.others, name = 'others'),
	path('lib/', views.lib, name = 'lib'),
	path('scilab/', views.scilab, name = 'scilab'),
	path('complab/', views.complab, name = 'complab'),
	path('hostel/', views.hostel, name = 'hostel'),
	
]