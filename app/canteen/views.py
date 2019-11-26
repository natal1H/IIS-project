from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from canteen.models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from django.http import HttpResponseRedirect

from canteen.forms import SignUpForm

from django.contrib.auth import login, authenticate


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


def signup(request):
	if request.method=='POST':
		
		form = SignUpForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')

			print(username)
			raw_password = form.cleaned_data.get('password1')

			firstname 	= form.cleaned_data.get('firstname')
			surname 	= form.cleaned_data.get('surname')
			address 	= form.cleaned_data.get('address')
			email		= form.cleaned_data.get('email')
			telephone	= form.cleaned_data.get('telephone')

			user = authenticate(username=username, password=raw_password)
			

			login (request, user)
			user_instance=User.objects.filter(username=username).first()
			print(user_instance)
			Person.objects.create(user=user_instance, firstname=firstname, surname=surname, address= address, telephone=telephone)


			return redirect('login_url')
	else:
		form=SignUpForm()
	
	return render(request, 'registration/register.html', {'form': form})

def logged_view(request):
	context = {

	}

	return render(request, 'registration/logged_on.html', context)

def contact_view(request):
	context = {

	}
	return render(request, 'contact.html', context)


def  profile_view(request):
	context = {

	}
	return render(request, 'profile.html', context)



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
		menu = Menu_items.objects.filter(id_menu=id)
	except Facility_menus.DoesNotExist:
		raise Http404
	item_objs = []

	for i in menu:
		#print(i)
		item_objs.append(i.id_item)
		
	facility = Facility_menus.objects.get(id_menu=id)

	context = {
		"item_objs": item_objs,
		"menu": Menu.objects.get(id_menu=id),
		"id_facility": id, # TODO: nie je toto id_menu?
		"id_menu": id,
		"facility": facility.id_facility # TODO: WHY DOES THIS WORK??
	}

	return render(request, 'menu_detail.html', context)

def add_to_cart(request, id_item, id_facility):
	
	cart_id=request.session.get("cart_id", None)
	qs=Food_order.objects.filter(id_food_order=cart_id)


	if qs.count()==1:
		cart_obj=qs.first()
		print ("it is already created")

		#
		food_order_instance		=Food_order.objects.filter(id_food_order=cart_obj.id_food_order).first()
		food_order_item_instance=Item.objects.filter(id_item=id_item).first()
		
		
		Food_order_item.objects.create(id_food_order=food_order_instance, id_item=food_order_item_instance)



		
	else:
		print ("Now we are makin new order")
		facility_instance		=Facility.objects.filter(id_facility=id_facility).first()
		food_order_item_instance=Item.objects.filter(id_item=id_item).first()

		#Creates new food order
		if request.user.is_authenticated:

			person_instance		=Person.objects.filter(user=request.user).first()
			food_order_instance	=Food_order.objects.create(facility=facility_instance, person=person_instance)#Creates new food order
		else:
			food_order_instance	=Food_order.objects.create(facility=facility_instance)


		
		Food_order_item.objects.create(id_food_order=food_order_instance, id_item=food_order_item_instance)#adds the item to the order
		

		
		request.session['cart_id']=food_order_instance.id_food_order

		#TOCONTINUE 
		

	
	context = {

	}

	#TODO order, checkout etc. and all
	return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #stays on the same page
	

def remove_from_cart(request):
	#TODO
	pass

def all_orders_view(request):
	#TODO
	pass





def order_view(request):#basically a cart
	
	#if request.user.is_authenticated:
		#print ("Yes, he is")

	cart_id=request.session.get("cart_id", None)
	qs=Food_order.objects.filter(id_food_order=cart_id)

	if qs.count()==1:
		cart_obj=qs.first()
		print ("it is already created")
	else:
		cart_obj=Food_order.objects.create()
		request.session['cart_id']=cart_obj.id_food_order



	context={

	}

	return render(request, 'order.html', context)