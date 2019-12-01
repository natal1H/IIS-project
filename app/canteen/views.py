from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


from django.http import HttpResponseRedirect

from .forms import *

from django.contrib.auth import login, authenticate

from django.views.generic import *

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
			Person.objects.create(user=user_instance, firstname=firstname, surname=surname, address= address, telephone=telephone, role='r')


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






def dynamic_facility_view(request, id):

	try:
		menu=Facility_menus.objects.filter(id_facility=id)
	except Facility.DoesNotExist:
		raise Http404
	
	
	menu_objs=[]
	for i in menu:
		menu_objs.append(i.id_menu)

	

	"""
	meals=testItem.objects.all()
	facility_meals=[]
	for item in meals:
		if item.Facility.id_facility==id:
			facility_meals.append(item)
	"""
	#getting meals that belongs to that facility


	# handling the nonexistent page
	try:
		obj =Facility.objects.get(id_facility=id)
	except Facility.DoesNotExist:
		raise Http404

	context = {
		#"meals":facility_meals,
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
		
	facility = Facility_menus.objects.filter(id_menu=id).first()

	facility_menus_instance = Facility_menus.objects.filter(id_menu=id).first()
	print(facility_menus_instance.id_facility.id_facility)
	#facility_instance = Facility.objects.filter(id_facility=facility_menus_instance.id_facility)


	context = {
		"item_objs": item_objs,
		"menu": Menu.objects.get(id_menu=id),
		"id_facility": facility_menus_instance.id_facility.id_facility, # TODO: nie je toto id_menu?
		"id_menu": id,
		"facility": facility.id_facility # TODO: WHY DOES THIS WORK??
	}

	return render(request, 'menu_detail.html', context)

def add_to_cart(request, id_item, id_facility):
	
	cart_id=request.session.get("cart_id", None)
	qs=Food_order.objects.filter(id_food_order=cart_id, status='o')


	if qs.count()==1:
		cart_obj=qs.first()
		print ("it is already created")

		#
		food_order_instance		=Food_order.objects.filter(id_food_order=cart_obj.id_food_order).first()
		food_order_item_instance=Item.objects.filter(id_item=id_item).first()
		
		
		food_order_item_instance_from_mm_table=Food_order_item.objects.filter( id_food_order=food_order_instance, id_item=food_order_item_instance ) 

		if food_order_item_instance_from_mm_table.count()==1:
			quantity=food_order_item_instance_from_mm_table.first().quantity+1
			print(quantity)
			Food_order_item.objects.filter( id_food_order=food_order_instance, id_item=food_order_item_instance ).update(quantity=quantity)
			#Food_order.objects.filter(id_food_order=cart_id, status='o').update(status='a')
		else:
			Food_order_item.objects.create(id_food_order=food_order_instance, id_item=food_order_item_instance)



		
	else:
		print ("Now we are makin new order")
		facility_instance		=Facility.objects.filter(id_facility=id_facility).first()
		food_order_item_instance=Item.objects.filter(id_item=id_item).first()

		#Creates new food order
		if request.user.is_authenticated:

			person_instance		=Person.objects.filter(user=request.user).first()
			food_order_instance	=Food_order.objects.create( facility=facility_instance, person=person_instance, status='o')#Creates new food order
		else:
			food_order_instance	=Food_order.objects.create( facility=facility_instance, status='o')


		
		Food_order_item.objects.create(id_food_order=food_order_instance, id_item=food_order_item_instance)#adds the item to the order
		

		
		request.session['cart_id']=food_order_instance.id_food_order

		#TOCONTINUE 


	#TODO order, checkout etc. and all  almost done, but needs to be finalized and tested
	return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #stays on the same page


def remove_from_cart(request, id_item, id_facility):

	if request.user.is_authenticated:

		item_instance		=Item.objects.filter(id_item=id_item).first()
		person_instance		=Person.objects.filter(user=request.user).first()
		food_order_instance =Food_order.objects.filter(person=person_instance, status='o').first()

		delete_instance		=Food_order_item.objects.filter(id_item=item_instance ,id_food_order=food_order_instance).first()
		
		if delete_instance.quantity==1:
			delete_instance.delete()
		else:
			quantity=delete_instance.quantity-1
			print(quantity)
			Food_order_item.objects.filter(id_item=item_instance ,id_food_order=food_order_instance).update(quantity=quantity)
			

		"""
		quantity=food_order_item_instance_from_mm_table.first().quantity+1
		print(quantity)
		Food_order_item.objects.filter( id_food_order=food_order_instance, id_item=food_order_item_instance ).update(quantity=quanti
		"""
		

		#print(delete_instance)
		#food_order_instance	=Food_order.objects.create(facility=facility_instance, person=person_instance)

	#TODO for unathorized users
	else: 
		cart_id=request.session.get("cart_id", None)
		food_order_instance=Food_order.objects.filter(id_food_order=cart_id, status='o').first()


		item_instance		=Item.objects.filter(id_item=id_item).first()

		delete_instance		=Food_order_item.objects.filter(id_item=item_instance ,id_food_order=food_order_instance).first()
		
		if delete_instance.quantity==1:
			delete_instance.delete()
		else:
			quantity=delete_instance.quantity-1
			print(quantity)
			Food_order_item.objects.filter(id_item=item_instance ,id_food_order=food_order_instance).update(quantity=quantity)


	return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #stays on the same page

	#TODO

#current order
def cart_view(request):
	#TODO it doesnt work
	#might not work with migrations sometimes
	if request.user.is_authenticated:
		person_instance				=Person.objects.filter(user=request.user).first()
		food_order_instance 		=Food_order.objects.filter(person=person_instance, status='o').first()
		#print(food_order_instance.status)
		food_order_items_list		=Food_order_item.objects.filter(id_food_order=food_order_instance)
		#print(food_order_instance.id_food_order)
		#print(person_instance)
		#print(food_order_items_list)
		#print(food_order_items_list)
		if food_order_instance is None:
			facility_instance=  None
		else:
			facility_instance = food_order_instance.facility

		unregistered=False

	else: 
		unregistered=True
		cart_id=request.session.get("cart_id", None)
		food_order_instance = Food_order.objects.filter(id_food_order=cart_id, status='o').first()
		food_order_items_list = Food_order_item.objects.filter(id_food_order=food_order_instance)
		print(food_order_instance)
		if food_order_instance is None:
			facility_instance=  None
		else:
			facility_instance = food_order_instance.facility
	
	context={
		"food_order_instance":food_order_instance,
		"food_order_items_list":food_order_items_list,
		"facility_instance":facility_instance,
		"unregistered":unregistered,
	}

	return render(request, 'cart.html', context)

def pay_view(request):


	

	if request.user.is_authenticated:
		
		person_instance				=Person.objects.filter(user=request.user).first()
		Food_order.objects.filter(person=person_instance, status='o').update(status='a')
		#print(food_order_instance.status)
		#food_order_instance.status='a'
		#print(food_order_instance.status)
	else: 
		cart_id=request.session.get("cart_id", None)
		
		#TODO think about unregistered payment
		my_form=Pay_form()
		if request.method=="POST":
			
			my_form=Pay_form(request.POST)
			
			if my_form.is_valid():
				print(my_form.cleaned_data["telephone"])

				person_instance=Person.objects.create(**my_form.cleaned_data)
				Food_order.objects.filter(id_food_order=cart_id, status='o').update(status='a',person=person_instance)
				context={

				}
				return render(request, 'paid.html', context)

			else:
				print(my_form.errors)
			
		context={
			"form":my_form
		}

		return render(request, 'pay_unregistered.html', context)
	#TODO

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def pay_view_unreg(request):
	if request.user.is_authenticated:
		raise PermissionDenied()  
	

	my_form=Pay_form()



	pass


#this is basically all orders view

def order_view(request):#basically a cart
	"""
	if request.user.is_authenticated:
		print ("Yes, he is")
	
	cart_id=request.session.get("cart_id", None)
	qs=Food_order.objects.filter(id_food_order=cart_id)

	if qs.count()==1:
		cart_obj=qs.first()
		print ("it is already created")
	else:
		cart_obj=Food_order.objects.create()
		request.session['cart_id']=cart_obj.id_food_order

	"""

	if request.user.is_authenticated:
		
		person_instance	=Person.objects.filter(user=request.user).first() 
		food_order_qs	=Food_order.objects.filter(person=person_instance)
		#print(food_order_qs)



		food_order_ordered	 =Food_order.objects.filter(person=person_instance, status='o')
		food_order_approved	 =Food_order.objects.filter(person=person_instance, status='a')
		food_order_canceled	 =Food_order.objects.filter(person=person_instance, status='c')
		food_order_delivered =Food_order.objects.filter(person=person_instance, status='d')
		
		context={
			"food_order_ordered":food_order_ordered,
			"food_order_approved":food_order_approved,
			"food_order_canceled":food_order_canceled,
			"food_order_delivered":food_order_delivered,
		}

	else:

		context = {
			"message":"it is not here"

		} 


	return render(request, 'order.html', context)

@login_required
def  profile_view(request):

	if request.user.is_authenticated:
		person_instance	= Person.objects.filter(user=request.user).first()

		context = {
			"person": person_instance,
			"role": person_instance.role
		}
	else: 
		raise Http404
	
	return render(request, 'profile.html', context)

def admin_view(request):

	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()

		if person_instance.role != 'a':
			raise Http404
		context = {
			"role":person_instance.role
		}
	else: 
		raise Http404


	return render(request, 'admin_view.html', context)
	#TODO


def admin_edit_users(request):
	#TODO
	pass


class Food_order_update_view(generic.UpdateView):
    template_name = 'food_order_update_view.html'
    form_class = Food_order_form
    def get_object(self):
        id = self.kwargs.get("id")
        
        return get_object_or_404(Food_order, id_food_order=id)

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)


class Food_order_delete_view(DeleteView):
    template_name = 'food_order_delete_view.html'
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Food_order, id_food_order=id)

    def get_success_url(self):
        return '../food_order'

"""
class Food_order_list_view(ListView):
    template_name = 'Food_order_list.html'
    queryset = list(Food_order.objects.all())
"""
class person_update_view(generic.UpdateView):
    template_name = 'person_update.html'
    form_class = person_form
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Person, id_person=id)

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)



def  person_list_view(request):


	if request.user.is_authenticated:

		person_instance			=Person.objects.filter(user=request.user).first()
		person_instance_list	=Person.objects.all()
		


		if person_instance.role == 'a':
			
			context={
				"person_instance_list":person_instance_list
			}
		else:
			raise Http404

		
	else: 
		raise Http404

	

	return render(request, 'person_list_view.html', context)


class user_update_view(generic.UpdateView):
	
	pass

def  food_order_list_view(request):
	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_operator()
		person_instance.is_driver()
		food_order_list=Food_order.objects.all()

		context={
			"food_order_list":food_order_list
		}
	else:
		raise Http404


	return render(request, 'Food_order_list.html', context)

def driver_view(request):

	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_driver()

		driver_orders_list=Food_order.objects.filter(delivered_by=person_instance, status='a')


		print(driver_orders_list)

		if person_instance.role == 'a' or person_instance.role == 'd':
			context = {
			"driver_orders_list":driver_orders_list,
			"role":person_instance.role
			}
		else:
			raise Http404


		

	else: 
		raise Http404


	return render(request, 'driver_view.html', context)	


def driver_food_order_info(request, id):

	food_order_instance=Food_order.objects.filter(id_food_order=id).first()
	
	person_customer_instance=food_order_instance.person

	context={
		'food_order_instance': food_order_instance,
		'person_customer_instance': person_customer_instance
	}
	return render(request, 'driver_food_order_info.html', context)	

@login_required
def driver_deliver(request, id):

	print("hello")
	Food_order.objects.filter(id_food_order=id).update(status='d')
	
	
	return redirect('driver_view')	


def operator_view(request):
	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()

		if person_instance.role == 'a' or person_instance.role == 'o':
			context = {
				"role":person_instance.role
			}
		else:
			raise Http404

	else: 
		raise Http404


	return render(request, 'operator_view.html', context)	

def food_list_view(request): 
	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_operator()

	else:
		raise Http404

	food_list=Item.objects.all()



	context={
		"food_list":food_list

	}

	return render(request, 'food_list_view.html', context)




class food_update_view(generic.UpdateView):
    template_name = 'food_update_view.html'
    form_class = Food_form
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Item, id_item=id)

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)

class food_delete_view(DeleteView):
    template_name = 'food_delete_view.html'
    form_class = Food_form

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Item, id_item=id)

    def get_success_url(self):
        return '../food_list_view'

class food_create_view(CreateView):
	
    template_name = 'food_create_view.html'
    form_class = Food_form
    queryset = Item.objects.all() 

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
	
    def get_success_url(self):
        return '../food_list_view'

class menu_create_view(CreateView):
    template_name = 'menu_create_view.html'
    form_class = Menu_form
    queryset = Menu.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
	
    def get_success_url(self):
        return '../menu_list_view'


class menu_update_view(UpdateView):

    template_name = 'menu_update_view.html'
    form_class = Menu_form
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Menu, id_menu=id)

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)


class menu_delete_view(DeleteView):
    template_name = 'menu_delete_view.html'
    form_class = Menu_form

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Menu, id_menu=id)

    def get_success_url(self):
        return '../menu_list_view'


def menu_list_view(request): 

	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_operator()

	menu_instance_list=Menu.objects.all()

	context={
		"menu_instance_list":menu_instance_list,
	}
	
	return render(request, 'menu_list_view.html', context)	


def facility_list_staff_view(request):
	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_operator()

	facility_instance_list=Facility.objects.all()

	context={
		"facility_instance_list":facility_instance_list,
	}
	
	return render(request, 'facility_staff_view.html', context)	


	pass


class facility_create_view(CreateView):
    template_name = 'facility_create_view.html'
    form_class = Facility_form
    queryset = Facility.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
	
    def get_success_url(self):
        return '../facility_list_staff_view'


class facility_update_view(UpdateView):

    template_name = 'facility_update_view.html'
    form_class = Facility_form
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Facility, id_facility=id)

    def form_valid(self, form):
        
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        id = self.kwargs.get("id")
        return '../facility_update_view/'+str(id)

class facility_delete_view(DeleteView):
    template_name = 'facility_delete_view.html'
    form_class = Facility_form

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Facility, id_facility=id)

    def get_success_url(self):
        return '../facility_list_staff_view'


def facility_menus_list_staff(request, id):

	#facility_instance=Facility.objects.filter(id_facility=id)
	facility_menus_instance_list=Facility_menus.objects.filter(id_facility=id)

	print(facility_menus_instance_list)


	menu_list=[]
	
	for x in facility_menus_instance_list:
		menu_list.append(x.id_menu)


	#menus_instance_list=Menu.objects.filter(id_menu=facility_menus_instance_list.id_menu)
	
	context={
		"menu_list": menu_list
	}
	return render(request, 'facility_menus_list_staff.html', context)

def facility_menus_items_list_staff(request, id):

	#menu_instance=Menu.objects.filter(id_menu=id)
	facility_menus_items_list=Menu_items.objects.filter(id_menu=id)

	#print(facility_menus_items_list)


	item_list=[]
	
	for x in facility_menus_items_list:
		item_list.append(x.id_item)


	#menus_instance_list=Menu.objects.filter(id_menu=facility_menus_instance_list.id_menu)
	
	context={
		"item_list": item_list,
		"id_menu":id
	}
	return render(request, 'facility_menus_items_list_staff.html', context)

def delete_from_menu(request, id_menu, id_item):

	if request.user.is_authenticated:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_operator()
	else: 
		PermissionDenied()
		return render(request, 'error_access.html', {})
	

	delete_instance=Menu_items.objects.filter(id_menu=id_menu, id_item=id_item).first()
	delete_instance.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER')) #stays on the same page

def controlPermissions(request, bool_var, person_instance):
	if bool_var:
		person_instance		=Person.objects.filter(user=request.user).first()
		person_instance.is_admin()
		person_instance.is_operator()
	else: 
		PermissionDenied()
		return render(request, 'error_access.html', {})

@login_required
def profile_edit(request):

	person_instance		=Person.objects.filter(user=request.user).first()
	if request.method=='POST':
		person_instance		=Person.objects.filter(user=request.user).first()
		user_instance= request.user


		form = EditProfileForm(request.POST or None)

		if form.is_valid():
			#form.save()
			#username = form.cleaned_data.get('username')
			firstname 	= form.cleaned_data.get('firstname')
			surname 	= form.cleaned_data.get('surname')
			address 	= form.cleaned_data.get('address')
			email		= form.cleaned_data.get('email')
			telephone	= form.cleaned_data.get('telephone')

			Person.objects.filter(id_person=person_instance.id_person).update(	firstname=firstname,
																				surname=surname,
																				address=address,
																				telephone=telephone, 
																				email=email)
			
			person_instance		=Person.objects.filter(user=request.user).first()

			"""
			user = authenticate(username=username, password=raw_password)
			

			login (request, user)
			user_instance=User.objects.filter(username=username).first()
			print(user_instance)
			Person.objects.create(user=user_instance, firstname=firstname, surname=surname, address= address, telephone=telephone, role='r')


			return redirect('login_url')
			"""



	else:
		form=EditProfileForm()
	
	context={
		'form': form,
		'user_profile':request.user,
		'person':person_instance,
	
	}

	return render(request, 'profile_edit.html', context)



