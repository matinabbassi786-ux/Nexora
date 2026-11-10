from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from security  import User_authenticated


@api_view()
def index(request):

    if  User_authenticated.authenticated(request):
        return  User_authenticated.authenticated(request)  
    Data ={}
    return Response(Data,)