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