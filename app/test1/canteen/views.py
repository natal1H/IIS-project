from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from canteen.models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from django.http import HttpResponseRedirect


# Create your views here.


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

	try:
		menu=Facility_menus.objects.filter(id_facility=id)
	except Facility.DoesNotExist:
		raise Http404
	
	
	#print(menu)

	#print(i.id_facility.id_facility)
	print (menu)
	menu_objs=[]
	for i in menu:
		menu_objs.append(i.id_menu)

	print(menu_objs)
	


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
		"object":obj,
		"menu_objs":menu_objs
	}
	return render(request, 'facility_detail.html', context)

def menu_view(request, id): 

	try:
		menu=Menu_items.objects.filter(id_menu=id)
	except Facility_menus.DoesNotExist:
		raise Http404
	item_objs=[]

	for i in menu:
		item_objs.append(i.id_item)
		
	
	context={
		"item_objs":item_objs
	}

	return render(request, 'menu_detail.html', context)

def add_to_cart(request, id):
	#it somehow works
	print (id)
	context = {

	}
	#TODO order, checkout etc. and all
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#stays on the same page
	#return render(request, 'cart.html', context)


def order_view(request):#basically a cart
	
	#if request.user.is_authenticated:
		#print ("Yes, he is")

	cart_id=request.session.get("cart_id", None)
	qs=testOrder.objects.filter(id_order=cart_id)

	if qs.count()==1:
		cart_obj=qs.first()
		print ("it is already created")
	else:
		cart_obj=testOrder.objects.create()
		request.session['cart_id']=cart_obj.id_order


	context={

	}

	return render(request, 'order.html', context)