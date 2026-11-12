from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index ,name="API" ),
    path('loging/',views.Login,name="Login"),
     

]
