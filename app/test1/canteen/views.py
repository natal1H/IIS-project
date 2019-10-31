from django.shortcuts import render
from django.views import generic
from canteen.models import *

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

    context = {
        "object": obj,
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
