from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

#basic
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_view, name='search'),
    path('contact',views.contact_view, name='contact'),
    path('facility/<int:id>', views.dynamic_facility_view, name='facility-view'),
    path('menu/<int:id>', views.menu_view, name='menu'),
    path('order',views.order_view, name='order'),
    path('cart',views.cart_view, name='cart'),
    path('pay',views.pay_view, name='pay'),
    path('add_to_cart/<int:id_item>/<int:id_facility>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id_item>/<int:id_facility>', views.remove_from_cart, name='remove_from_cart'),

]
#fot admin processes
urlpatterns+=[
   
    path('admin_view', views.admin_view, name='admin_view'),
    path('driver_view', views.driver_view, name='driver_view'),
    path('operator_view', views.operator_view, name='operator_view'),
    path('food_order/', views.food_order_list_view, name='food_order'),
    path('food_order_update/<int:id>', views.Food_order_update_view.as_view(), name='food_order_update')

]

#user authentication
urlpatterns+=[
   
    path('register', views.signup, name='register'),
    path('login', LoginView.as_view(), name='login_url'),
    path('logged', views.logged_view, name='loggend_on'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile', views.profile_view, name='profile'),
    
]