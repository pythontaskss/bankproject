from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from bankapp.models import DistrictModel, BranchModel


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if not username:
            return render(request,'register.html')

        if not password:
            return render(request,'register.html')

        if not confirm_password:
            return render(request,'register.html')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.is_staff = False
                user.save()
                return redirect('login_user')
    else:
        print("this is not post method")
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # if not username:
        #     messages.info(request, 'enter username')
        #     return render(request,'login_user')

        # if not password:
        #     messages.info(request, 'enter password')
        #     return render(request,'login_user')



        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, 'Invalid username or password')
            print('invalid password or username')
            return redirect('login_user')

    else:
        return render(request, 'login.html')


def detail(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']


        if not name:
            return render(request,'detail.html')

        if not phone:
            return render(request,'detail.html')
        user = auth.authenticate(name=name, phone=phone)
        if user is not None:

            return redirect('form')
        else:
            # messages.info(request, 'submit accepted')
            return redirect('form')

    districtobj = DistrictModel.objects.all()
    branchobj = BranchModel.objects.all()
    return render(request, "detail.html", {"District": districtobj, "Branch": branchobj})


def new(request):
    return render(request, 'new.html')

def form(request):
    return render(request, 'form.html')



def logout_user(request):
    auth.logout(request)
    return redirect('home')
