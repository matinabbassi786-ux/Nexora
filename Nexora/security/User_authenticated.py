from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response



def authenticated(request):
    try:
        if request.user.is_authenticated:
            print("Yes is login")
        else:
            print("NO is login")
            pass
            # return redirect('/login/')
    except:
        pass