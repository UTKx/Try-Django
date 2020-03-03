from django.shortcuts import render, redirect
from myapp.forms import GareebForm
from myapp.models import Gareeb

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def addData(request):
    return render(request, 'add.html')

def getShow(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    password = request.GET.get('password')
    address1 = request.GET.get('address1')
    address2 = request.GET.get('address2')
    city = request.GET.get('city')
    state = request.GET.get('state')
    zip = request.GET.get('zip')
    data = email, password, address1, address2, city, state, zip
    return render(request, 'getshow.html', {'data': data})

def postShow(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip = request.POST.get('zip')
    data = email, password, address1, address2, city, state, zip
    return render(request, 'postshow.html', {'data': data})

def putData(request):
	if request.method == "GET":
		form = GareebForm(request.GET)
		if form.is_valid():
			try:
				form.save()
			except:
				print("Invalid Data!")
	else:
		form = GareebForm()
	return render(request, 'add.html', {'form': form})

def showData(request):
	data = Gareeb.objects.all()
	return render(request, 'show.html', {'data': data})

def delete(request, id):
    data = Gareeb.objects.get(id=id)
    if data.delete():
       return redirect('/showdata')