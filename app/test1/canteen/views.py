from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from canteen.models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from django.http import HttpResponseRedirect


# Create your views here.

"""
def home_view(request):
	obj = Facility.objects.all()  # list of objects
	context = {
		"object": obj,
	}
	return render(request, 'base.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
"""

"""
def search_view(request):
    search = request.POST.get('search')
    print(search)
    return render(request, 'search_success.html',{})
    
    
def login_view(request):
	return render(request, 'base.html',{})

"""

"""
#prints are just for debugging

def search_result_view(request):

    search =request.POST.get('search_form')
    print(search)
    objects = Facility.objects.all()
    for obj in objects:
        if search in obj.address or search in obj.name:
            print("hey it is here")
            print(obj.address)
            print(obj.name)

    #print(search)
    return render(request, 'search_success.html', {})

"""



def index(request):

    obj = Facility.objects.all()


    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        "object": obj,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)



def search_view(request):
	search=request.GET.get('search_form')

	objects = Facility.objects.all()

	corr_search_objs=[]

	for obj in objects:
		if search in obj.address or search in obj.name:
			corr_search_objs.append(obj)

	context = {
		"result":	search,
		"objects":	corr_search_objs
	}

	return render(request, 'search_result.html', context=context)

def register_view(request):

	context = {

	}

	if request.method =="POST":
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('login_url')


	else:
		form = UserCreationForm()

	return render(request, 'registration/register.html', {'form': form})


def logged_view(request):
	context = {

	}

	return render(request, 'registration/logged_on.html', context)

def contact_view(request):
	context = {

	}
	return render(request, 'contact.html', context)

def dynamic_facility_view(request, id):


	meals=testItem.objects.all()
	facility_meals=[]
	for item in meals:
		if item.Facility.id_facility==id:
			facility_meals.append(item)
	#getting meals that belongs to that facility


	# handling the nonexistent page
	try:
		obj =Facility.objects.get(id_facility=id)
	except Facility.DoesNotExist:
		raise Http404

	context = {
		"meals":facility_meals,
		"object":obj
	}
	return render(request, 'facility_detail.html', context)

def add_to_cart(request, id):
	#it somehow works
	print (id)
	context = {

	}
	#TODO order, checkout etc. and all
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#stays on the same page
	#return render(request, 'cart.html', context)
