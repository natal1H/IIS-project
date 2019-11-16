from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

#basic
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_view, name='search'),
    path('contact',views.contact_view, name='contact'),
    path('order',views.order_view, name='order'),

]

#user authentication
urlpatterns+=[
    path('facility/<int:id>', views.dynamic_facility_view, name='facility-view'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('register', views.register_view, name='register'),
    path('login', LoginView.as_view(), name='login_url'),
    path('logged', views.logged_view, name='loggend_on'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('menu/<int:id>', views.menu_view, name='menu')

]