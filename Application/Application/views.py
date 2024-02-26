from django.shortcuts import render
from django.http import HttpResponse
from Application.models import User_db , Password_db
import cryptocode
# Create your views here.
def encoded_message(message):
    key = "123456"
    encoded = cryptocode.encrypt(message,key)
    return encoded


def decoded_message(encoded_message):
    key = "123456"
    decoded = cryptocode.decrypt(encoded_message,key)
    return decoded

    
def math(request):
    return HttpResponse("This is demo application")

def Home(request):
    return render(request,'Home.html')

def signing(request):
    return render(request,'signing.html')

def Login(request):
    return render(request,'Login.html')

def Password(request):
    return render(request,'PasswordStorage.html')

def process_signing_data(request):
    UserName = request.POST['Username']
    Email = request.POST['email']
    Password = request.POST['password']
    PasswordAgain = request.POST['psw_repeat']
    if Password == PasswordAgain:
        new_user=User_db()   # It will creat the new user in a database.
        new_user.Name = UserName
        new_user.Email = Email
        new_user.Password =  encoded_message(Password)
        new_user.save()
        return render(request,'signing.html' , {'alert_message':'Your successfully registered'})
    else:
        return render(request,'signing.html' , {'alert_message':'Both password are not match'})

def login_data(request):
    Uname = request.POST['UserName']
    password = request.POST['password']
    try:
        check_database = User_db.objects.get(Name = Uname )
        print(decoded_message(check_database.password))
        if password == decoded_message(check_database.password):
            request.session['UserID']=check_database.id
            return render(request,'Login.html' , {'alert_message':'Your successfully login'})
        else:
            return render(request,'Login.html' , {'alert_message':'user name is correct but password is wrong'})
    except:
        return render(request,'Login.html' , {'alert_message':'Invalid user name'})

def add_password(request):
    ID = request.session['UserId']
    Name = request.session['SelectedPassword']

    try:
        check_DB = Password_db.objects.get(UserID = ID , UserName = Name)
        details = User_db.objects.all()
        return render(request,'PasswordStorage.html' , {'alert_message':'Your Password is saved','PasswordData':details})
    except:
        new_object = Password_db()
        details = User_db.objects.all()
        new_object.UserID = ID
        new_object.UserName = Name
        new_object.save()
        return render(request,'PasswordStorage.html' , {'alert_message':'Your Password Added','PasswordData':details})

