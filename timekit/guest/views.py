import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from .models import user, calender, User_signup
from django.test import TestCase

# View for signup user for chegg app



def user_logout(request):
    logout(request)
    return render(request, 'guest/timekit_login.html')
    # Redirect to a success page.
def app_signup(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_first_name = request.POST["first_name"]
        user_last_name = request.POST["last_name"]
        user_password = request.POST["password"]

        if not User_signup.objects.filter(email=user_email):
            create_user = User_signup.objects.create(
                            first_name = user_first_name,
                            last_name = user_last_name,
                            email = user_email,
                            password = user_password
            )

            return render(request, 'guest/welcome.html')
        else:
            messages.error(request, 'This email is already exist')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# View for login user for chegg app
def app_login(request):
    email = request.POST['email']
    password = request.POST["password"]
    user_email = User_signup.objects.filter(email=email)
    if user_email:
        user_email = User_signup.objects.get(email=email).email
        user_password = User_signup.objects.get(email=email).password
        if email == user_email and password == user_password:
            return render(request, 'guest/timekit.html')

        else:
            messages.error(request, 'User name or password are incorrect')
            return redirect('/')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# View for signup user on chegg dashboard
def usersubmit(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_first_name = request.POST["first_name"]
        user_last_name = request.POST["last_name"]
        user_password = request.POST["password"]

        try:
            if user.objects.filter(email=user_email):

                messages.error(request, 'User is already register with this email')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
                data = json.dumps({'email': user_email,
                                   'timezone': 'America/Los_Angeles',
                                   'first_name': user_first_name,
                                   'last_name': user_last_name,
                                   'password': user_password})
                login_response = requests.post('https://api.timekit.io/v2/users', headers=headers, data=data)
                decoded = login_response.json()
                guest_user = user.objects.create(first_name=decoded['data']['first_name'],
                                                email=decoded['data']['email'],
                                                last_name=decoded['data']['last_name'],
                                                created_at=decoded['data']['created_at'],
                                                updated_at=decoded['data']['updated_at'],
                                                timezone=decoded['data']['timezone'],
                                                api_token=decoded['data']['api_token']
                                               )
                guest_user.save()
                return render(request, 'guest/timekit_login.html')
        except:
            print 'inside usersubmit except'
            messages.error(request, 'user is alreay exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# View for login user on timekit dashboard
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST["password"]

        try:
            if user.objects.get(email=email):
                headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
                data = json.dumps({'email': email,
                                   'password': password})
                login_response = requests.post('https://api.timekit.io/v2/auth', headers=headers, data=data)
                decoded = login_response.json()
                print 'decode', decoded
                print '********',decoded['data']['api_token']
                user_data =user.objects.get(email=email)
                user_data.api_token = decoded['data']['api_token']
                user_data.save()
                if login_response.status_code == 200:
                    return render(request, 'guest/calender.html', {'email': email})
                else:
                    messages.error(request, 'You enter wrong email or password')
                    return redirect('/login/timekit')
            else:
                messages.error(request, 'You enter wrong email or password')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            messages.error(request, 'This user is not exist')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def usercalender(request):
    if request.method == "POST":
        name = request.POST["calender"]
        description = request.POST["description"]
        user_email = request.POST["email"]
        token = user.objects.get(email=user_email).api_token
        user_name = user.objects.get(email=user_email)

        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        auth = (user_email, token)
        data = json.dumps({'name': name,
                           'description': description})
        login_response = requests.post('https://api.timekit.io/v2/calendars', headers=headers, auth=auth, data=data)
        decoded = login_response.json()
        create_calender = calender.objects.create(cal_id=decoded['data']['id'],
                                                  name=decoded['data']['name'],
                                                  description=decoded['data']['description'],
                                                  user=user_name
                                                  )
        create_calender.save()
        return render(request, 'guest/findmy.html')
    else:
        return HttpResponse('Thanks for booking check your mail')


def entryview(request):
    if request.method == "POST":
        max_seats=request.POST['max_seats']
        min_cancel_time = request.POST['min_cancel_time']
        min_booking_time = request.POST['min_booking_time']
        max_booking_time = request.POST['max_booking_time']
        start = request.POST['start']
        end = request.POST['end']
        what = request.POST['what']
        where = request.POST['where']
        calendar_id = request.POST['calendar_id']
        description = request.POST['description']


        print "start", start
        print "end" , end

        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        auth = ('paresh@tudip.nl', '5143uAdoMihjm2IdJFOe1plE85SSDNTZ')
        data = json.dumps({'graph': "group_owner",
                           "action": "create",
                           "settings": {
                               "max_seats": max_seats,
                               "min_cancel_time": min_cancel_time,
                               "min_booking_time": min_booking_time,
                               "max_booking_time": max_booking_time
                           },
                           "event": {
                               "start": start,
                               "end": end,
                               "what": what,
                               "where": where,
                               "calendar_id": "56e3e8a7-5a12-448a-8e13-f17beee8e382",
                               "description": description
                           }
                           })
        login_response = requests.post('https://api.timekit.io/v2/bookings', headers=headers, auth=auth, data=data)
        decoded = login_response.json()
        print "login_response",login_response
        print "decoded",decoded
        print "inside if block"
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
         print 'inside else'
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
         # return HttpResponse('Thanks for booking check your mail')

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




# View for reset password
def reset_app_password(request):
    if request.method == "POST":
        email = request.POST['email']
        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        data = json.dumps({'email': email})
        login_response = requests.post('https://api.timekit.io/v2/users/resetpassword', headers=headers, data=data)
        return render(request,'guest/timekit_login.html')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#Update your details here
def update_content(request):
    if request.method == "POST":
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        token = user.objects.get(email=email).api_token
        auth = (email,token)

        if firstname == '':
            firstname = user.objects.get(email=email).first_name
            print "firstname",firstname
        else:
            print "user will get proper text"
        if lastname == '':
            lastname = user.objects.get(email=email).last_name
            print "lastname", lastname
        else:
            print "user will print proper text"


        headers = {'Timekit-App': 'chhegg', 'content-type': 'application/json', 'Accept': 'text/plain'}
        if password == confirm_password:
         data = json.dumps({'first_name': firstname,
                           'last_name': lastname,
                           'password': password})

         print "data" ,data

         login_response = requests.put('https://api.timekit.io/v2/users/me', headers=headers, auth= auth, data=data)
         # decoded = login_response.json()
         # print "decoded data is", login_response

         login = requests.get('https://api.timekit.io/v2/users/me',headers=headers,auth= auth)
         # print "login...........................@@@@@@@@@",login
         decoded = login.json()
         print "decoded data is this", decoded

         user_data = user.objects.get(email=email)
         user_data.first_name = decoded['data']['first_name']
         user_data.last_name = decoded['data']['last_name']
         user_data.created_at = decoded['data']['created_at']
         user_data.updated_at = decoded['data']['updated_at']
         user_data.updated_at = decoded['data']['updated_at']
         user_data.name = decoded['data']['name']
         user_data.timezone = decoded['data']['timezone']
         user_data.email = decoded['data']['email']

         user_data.save()




         # user_data.save()
         return render(request, 'guest/timekit_login.html')
        else:
            messages.error(request, 'password are not same')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))







#Update details
def update_details(request):
    return render(request,'guest/update_details.html')

def index(request):
    return render(request, "guest/welcome.html")

def signup(request):
    return render(request, 'guest/index.html')

def timekit_signup(request):
    return render(request, 'guest/timekit_signup.html')

def timekit_login(request):
    return render(request, 'guest/timekit_login.html')
def reset_password(request):
    return render(request,'guest/reset_password.html')


def math_booking(request):
    return render(request, 'guest/findmy.html')


def physics_booking(request):
    return render(request,'guest/findphysics.html')

def chemistry_booking(request):
    return render(request,'guest/findchemistry.html')




