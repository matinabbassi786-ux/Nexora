from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from security  import User_authenticated
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta
from rest_framework import status
from .Optimization import native

from Nexora.realtime.services import broadcast_test_event



@api_view(["GET"])
def index(request):
   
    broadcast_test_event("Hello from Django API")

    Data = {
        "status": "success",
        "message": "API executed successfully",
    }
    Data ={}
    return Response(Data)





@api_view(['GET', 'POST'])
def Login(request):
    # except:
        Data ={}
        Responseing  = Response(Data)
        
        Data ={
            "message":"Wlecome to Nexora Loging ",
            "UserName":"Enter The User Names",
            "Password":"Enter The Password",
            "Email":"Enter The Email ",
        }

        if request.method == 'POST':
            UserName = request.data.get('UserName', '')
            Password = request.data.get('Password', '')
            Email = request.data.get('Email', '')
            Errorsing = native.String_Check(UserName,Password,Email)

            Data.update({"Errorsing":Errorsing})          
        
        
        
        
        Responseing  = Response(Data)
        Responseing.set_cookie(
            key="totla_F", 
            value="0", 
            max_age=6, 
            httponly=True
        )
        return Responseing
    # except:
    #     Data={
    #         "message":"Nexora Not Woring please come back later"
    #         }
    #     Responseing  = Response(Data)
     
    #     return Responseing



@api_view(['GET', 'POST'])
def Login0(request):
    if request.method == 'POST':
        UserName = request.data.get('UserName', '')
        Password = request.data.get('Password', '')
        Email = request.data.get('Email', '')

        response_failed = Response({"message": "account done not exit plz sign in"},status=status.HTTP_200_OK)
        token = request.COOKIES.get("totla_F")

        if   token == None:
            Response.set_cookie(key="totla_F", value="0", max_age=60, httponly=True)

        else:
            
            print(token)
            

        
        if (len(UserName) >= 151) or (len(Password) >= 151) or (len(Email) >= 255)   :
            return Response({"Erro":"The character length is so must hight "})

        user = authenticate(request, username = UserName, password = Password)
        
        
        if user is not None:
            form = login(request, user)
            token = request.COOKIES.get("my00_cookie")
            print("\n")
            print(token)
            print("\n")
            
        else:

        
            return response_failed

        return Response({
            'UserName': UserName,
            'Password': Password,
            'Email': Email,
        })

    return Response({
        'Login': 'Welcome to login',
        'UserName': 'Enter the UserName',
        'Password': 'Enter the Password',
        'Email': 'Enter the Email',
    })



