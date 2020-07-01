from django.shortcuts import render, HttpResponse
from .models import Notice
# from .models import Student
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from .models import Homework


# Create your views here.
def index(request):
	notices = Notice.objects.all()
	parameters = {'notices' : notices}
	return render(request, 'mainsite/index.html', parameters)
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
	

def signin(request):
	if request.method == 'POST':
		#print('request is post')
		username = request.POST['username']
		password = request.POST['password']
		#print(username)
		#print(password)
		user = authenticate(request, username=username, password=password)
		if user is not None :
			#print('user is not none')
			login(request, user)
			return render(request, 'mainsite/personalInfo.html')
		else :
			param = {'error_message': 'Invalid Credentials'}
			return render(request, 'mainsite/index.html', param)
	
	else :
		#print('method is get')
		return render(request, 'mainsite/personalInfo.html')

def personalInfo(request):
	return render(request, 'mainsite/personalInfo.html')
def homework(request):
	hw = Homework.objects.filter(standard=request.user.student.standard, divison=request.user.student.divison)
	param = {'homework' : hw}
	return render(request, 'mainsite/homework.html', param)
def reportlaptop(request):
	return render(request, 'mainsite/report.html')
def reportmobile(request):
	return render(request, 'mainsite/academicreportmobile.html')
def videolecture(request):
	return render(request, 'mainsite/videolec.html')
def feedback(request):
	return render(request, 'mainsite/feedback.html')
	
def update(request):
	
	# if request.method == 'POST':
    #     name = request.POST['name']
    #     mis = request.POST['mis']
    #     std = request.POST['std']
    #     divison = request.POST['divison']
    #     doa = request.POST['doa']
    #     fatherName = request.POST['fatherName']
    #     fatherOccupation = request.POST['fatherOccupation']
    #     motherName = request.POST['motherName']
    #     motherOccupation = request.POST['motherOccupation']
    #     parentContact1 = request.POST['parentContact1']
    #     parentContact2 = request.POST['parentContact2']
    #     temporaryAddress = request.POST['temporaryAddress']
    #     parmenantAddress = request.POST['parmenantAddress']
    #     studentContact = request.POST['studentContact']
    # else:
		return render(request, 'mainsite/update.html')

def results(request):
	# return render(request, 'mainsite/results.html')
	
	return render(request, 'results.html')