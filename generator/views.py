from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request,'generator/home.html',{'password':'dbbkdsnb'})

def passwords(request):
   
     
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('0123456789')
    specialCharacters = list('~@-_%#')
    upperCharacters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    length = int(request.GET.get('length'))
    isNumber = request.GET.get('numbers')
    isspecial = request.GET.get('special')
    isuppercase = request.GET.get('uppercase')
    thepassword = ''
    if(isNumber == 'on'):
            thepassword += random.choice(numbers)
            length -= 1
    if(isspecial == 'on'):
            thepassword += random.choice(specialCharacters)
            length -= 1
    if(isuppercase == 'on'):
            thepassword += random.choice(upperCharacters)
            length -= 1
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})