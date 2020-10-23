from django.urls import path, include
from userapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('findpassword/', views.findpassword, name='findpassword'),
    path('password_done/', views.password_done, name='password_done'),
    path('password_reset/', views.password_reset, name='password_reset')
]

