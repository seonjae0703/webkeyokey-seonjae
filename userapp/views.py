from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'userapp/signup.html')

def findpassword(request):
    return render(request, 'userapp/findpassword.html')

def password_done(request):
    return render(request, 'userapp/password_done.html')

def password_reset(request):
    return render(request, 'userapp/password_reset.html')
