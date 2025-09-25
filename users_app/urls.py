from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redirect /users/ → /users/login/
    path('', RedirectView.as_view(url='login/', permanent=False)),

    # User authentication routes
    path('register/', views.register, name='register'),   
    path('login/', views.login_view, name='login'),      
    path('logout/', views.logout_view, name='logout'),    
    path('profile/', views.profile, name='profile'),      
]
