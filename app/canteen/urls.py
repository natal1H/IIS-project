from django.urls import path
from . import views

from django.contrib.auth.views import LoginView, LogoutView

#basic
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_view, name='search'),
    path('contact',views.contact_view, name='contact'),
    path('facility/<int:id>', views.dynamic_facility_view, name='facility-view'),
    path('facility_list_staff_view', views.facility_list_staff_view, name='facility_list_staff_view'),
    path('facility_create_view', views.facility_create_view.as_view(), name='facility_create_view'),
    path('facility_update_view/<int:id>', views.facility_update_view.as_view(), name='facility_update_view'),

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
    path('food_order/', views.food_order_list_view, name='food_order'),
    path('food_order_update/<int:id>', views.Food_order_update_view.as_view(), name='food_order_update'),
    path('food_order_delete/<int:id>', views.Food_order_delete_view.as_view(), name='food_order_delete'),
    path('person_update/<int:id>', views.person_update_view.as_view(), name='person_update'),
    path('person_list_view', views.person_list_view, name='person_list_view'),

    path('menu_list_view', views.menu_list_view, name='menu_list_view'),
    path('menu_create_view', views.menu_create_view.as_view(), name='menu_create_view'),
    path('menu_update_view/<int:id>', views.menu_update_view.as_view(), name='menu_update_view'),
    path('menu_delete_view/<int:id>', views.menu_delete_view.as_view(), name='menu_delete_view'),

]


urlpatterns+=[
    path('operator_view', views.operator_view, name='operator_view'),
    path('food_create_view', views.food_create_view.as_view(), name='food_create'),
    path('food_list_view', views.food_list_view, name='food_list_view'),
    path('food_update_view/<int:id>', views.food_update_view.as_view(), name='food_update_view'),
    path('food_delete_view/<int:id>', views.menu_create_view.as_view(), name='menu_create_view'),

]


#user authentication
urlpatterns+=[
   
    path('register', views.signup, name='register'),
    path('login', LoginView.as_view(), name='login_url'),
    path('logged', views.logged_view, name='loggend_on'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile', views.profile_view, name='profile'),
    
]