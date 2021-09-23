from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from trello_app.models import *
# Create your views here.
#ORM: Object Relational Mapping
#django provides a rich API

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'pages/home.html')

def dashboard(request):
    #get the user
    user = request.user
    #find the boards crated by this user
    # boards = Board.objects.filter(user=user)
    boards = user.board_set.all()
    #find all list created by this user
    # lists = TaskList.objects.filter(board__in=boards)
    #find all the task
    # tasks = Task.objects.filter(list__in=lists)
    # return render(request, 'pages/dashboard.html', {'boards': boards, 'lists': lists, 'tasks':tasks})
    return render(request, 'pages/dashboard.html', {'boards': boards})
def register(request):
    if request.method == "POST":
        # form = UserCreationForm(data = request.POST)
        form = CreateUserForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: form = CreateUserForm()
    return render(request, 'pages/register.html', {'form' : form})

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        # chack is user exist or not
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #login
        if user is not None :
            auth_login(request, user)
            # redirect to the dashboard
            return redirect('dashboard')
        else:
            # provide error message
            messages.error(request, 'Username or password is incorrect') 
    return render(request, 'pages/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')