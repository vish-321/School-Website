from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'mainsite/index.html')
	# return HttpResponse('Hello')


def geninfo(request):
	# return render(request, 'def index(request):
	return render(request, 'mainsite/geninfo.html')
	# return HttpResponse('Hello')')
	# return HttpResponse('Hello')


def sctu(request):
	return render(request, 'mainsite/sctu.html')
	
def infra(request):
	return render(request, 'mainsite/infra.html')

def prmsg(request):
	return render(request, 'mainsite/prmsg.html')



def procedure(request):
	return render(request, 'mainsite/procedure.html')

def age(request):
	return render(request, 'mainsite/age.html')

def academic(request):
	return render(request, 'mainsite/academic.html')

def others(request):
	return render(request, 'mainsite/others.html')
	
def lib(request):
	return render(request, 'mainsite/lib.html')
	
def scilab(request):
	return render(request, 'mainsite/scilab.html')
	
def complab(request):
	return render(request, 'mainsite/complab.html')
	
def hostel(request):
	return render(request, 'mainsite/hostel.html')
	