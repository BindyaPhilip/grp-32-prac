from django.urls import path  # Import Django's path function to define URL patterns
from . import views  # Import all views from the current directory's views module
from django.contrib.auth import views as auth_views  # Import Django's authentication views with an alias
from .views import RegisterUserAPIView  # Import a specific view for registering users via API

# Define URL patterns for the application
urlpatterns = [
    # User login and logout views
    path('login_user/', views.login_user, name="login"),  # URL for user login, linked to login_user view
    path('logout_user/', views.logout_user, name='logout'),  # URL for user logout, linked to logout_user view
    
    # User registration view
    path('register_user/', views.register_user, name='register'),  # URL for registering a user, linked to register_user view
    
    # Profile and general views
    path('profile/', views.profile, name='profile'),  # URL for viewing user profile, linked to profile view
    path('about/', views.showAbout, name='about'),  # URL for 'About' page, linked to showAbout view
    path('payment/', views.showPayment, name='payment'),  # URL for payment page, linked to showPayment view
    path('menu/', views.showMenu, name='menu'),  # URL for menu page, linked to showMenu view
    
    # Home page view
    path('', views.showHome, name='home'),  # Root URL (homepage), linked to showHome view
    
    # Menu category view
    path('menu/<category>/', views.menuByCategory, name='menuByCategory'),  # URL for viewing menu items by category
    
    # Cart management views
    path('addCart/<str:id>/', views.addCart, name='addCart'),  # URL to add item to cart by its id
    path('Cart/', views.display, name='Cart'),  # URL to display the cart
    path('checkout/', views.checkout, name='checkout'),  # URL for checkout page
    path('payments/', views.payments, name='payments'),  # URL for handling payments
    
    # Increase or reduce cart item quantities
    path('add/<int:id>/', views.add, name='add'),  # URL to increase quantity of item in cart by id
    path('reduce/<int:id>/', views.reduce, name='reduce'),  # URL to reduce quantity of item in cart by id
    
    # Search and delete items from cart
    path('search_item/', views.search_item, name='search_item'),  # URL to search for an item
    path('delete/<str:id>/', views.delete_from_cart, name='delete_from_cart'),  # URL to delete an item from the cart by its id
    
    # Payment-related views
    path('charge/', views.charge, name="charge"),  # URL to charge the customer (e.g., for online payments)
    
    # Password reset view using Django's built-in authentication view
    path('reset-password/', auth_views.PasswordResetView.as_view(), name="password_reset"),  # URL for password reset
    
    # Orders and payment methods views
    path('orders/', views.show_orders, name="orders"),  # URL to show user orders
    path('cod/', views.cash_on_delivery, name='cash_on_delivery'),  # URL for Cash on Delivery payment option
    
    # API for registering users
    path('api/register/', RegisterUserAPIView.as_view(), name='register'),  # API endpoint for user registration using RegisterUserAPIView
]
