from django.urls import path
from . import views 

app_name = 'myapp1'

urlpatterns = [
    path('', views.home,  name= 'home'),
    path('search/', views.search , name = 'search')
]