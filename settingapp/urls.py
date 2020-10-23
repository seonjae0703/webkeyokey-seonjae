from django.urls import path, include
from settingapp import views

urlpatterns = [
    path('bye/', views.bye, name='bye'),
    path('option/', views.option, name='option'),
]